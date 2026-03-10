# Coding Standards

To maintain a high-quality, professional codebase, all contributors must adhere to these standards.

## 🐍 Python Standards

-   **Style**: Adhere to [PEP 8](https://peps.python.org/pep-0008/).
-   **Naming**:
    -   Classes: `PascalCase`
    -   Functions/Variables: `snake_case`
    -   Constants: `UPPER_SNAKE_CASE`
-   **Docstrings**: Use **Google Style** docstrings.
    ```python
    def my_function(param1: int, param2: str) -> bool:
        """
        Brief description of the function.

        Args:
            param1: Description of param1.
            param2: Description of param2.

        Returns:
            Description of the return value.
        """
    ```
-   **Type Hinting**: Always use type hints for function signatures.

## 🎨 CSS & Frontend

-   **Framework**: Use Tailwind CSS utility classes.
-   **Custom CSS**: Minimize custom CSS; use `@apply` in CSS files if necessary.
-   **Templates**: Keep logic in templates to a minimum. Delegate complex presentation logic to template tags or view helpers.

## 💾 Database & Models

-   **Naming**: Table names should be explicit. If migrating from Laravel, ensure `db_table` matches legacy names if necessary.
-   **Soft Delete**: Inherit from `SoftDeleteModel` for all entities that should not be permanently deleted by default.

## 🚀 Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
- `feat: ...` for new features
- `fix: ...` for bug fixes
- `docs: ...` for documentation changes
- `refactor: ...` for code changes that neither fix a bug nor add a feature
