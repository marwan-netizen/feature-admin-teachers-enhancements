import uuid
import logging
from django.db import transaction
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from .models import OnlineSession, Assignment, AssignmentAttachment, AssignmentSubmission, SubmissionVersion, Classes
from accounts.models import Teacher, Student

logger = logging.getLogger(__name__)

class ClassroomService:
    def create_online_session(self, teacher_user, class_id, topic, start_time, duration):
        teacher = get_object_or_404(Teacher, user=teacher_user)
        room_name = str(uuid.uuid4())

        return OnlineSession.objects.create(
            class_info_id=class_id,
            teacher=teacher,
            topic=topic,
            room_name=room_name,
            start_time=start_time,
            duration=duration,
            join_url=f"https://meet.jit.si/{room_name}"
        )

    def create_assignment(self, teacher_user, class_id, title, description, due_date, attachments):
        teacher = get_object_or_404(Teacher, user=teacher_user)

        with transaction.atomic():
            assignment = Assignment.objects.create(
                class_info_id=class_id,
                teacher=teacher,
                title=title,
                description=description,
                due_date=due_date
            )

            for f in attachments:
                path = default_storage.save(f'assignments/{assignment.id}/{f.name}', f)
                AssignmentAttachment.objects.create(
                    assignment=assignment,
                    file_path=path,
                    file_name=f.name
                )
        return assignment

    def submit_assignment(self, student_user, assignment_id, content, file):
        student = get_object_or_404(Student, user=student_user)
        assignment = get_object_or_404(Assignment, id=assignment_id)

        with transaction.atomic():
            submission, created = AssignmentSubmission.objects.get_or_create(
                assignment=assignment,
                student=student,
                defaults={'status': 'submitted'}
            )
            if not created:
                submission.status = 'submitted'
                submission.save()

            version_num = SubmissionVersion.objects.filter(submission=submission).count() + 1
            file_path = None
            if file:
                file_path = default_storage.save(f'submissions/{submission.id}/{file.name}', file)

            return SubmissionVersion.objects.create(
                submission=submission,
                content=content,
                file_path=file_path,
                version=version_num
            )

    def grade_submission(self, teacher_user, submission_id, grade, comment):
        # Teacher check is handled at view level for now, but could be reinforced here
        submission = get_object_or_404(AssignmentSubmission, id=submission_id)
        submission.grade = grade
        submission.teacher_comment = comment
        submission.status = 'graded'
        submission.save()
        return submission
