# Intentional Ruff Errors

The following 4 errors were introduced in `vibe/core/logger.py` to be caught by `uv run ruff check .`:

| # | Rule | Location | Description |
|---|------|----------|-------------|
| 1 | `I001` | line 1 | Import block unsorted — `import logging` placed before `from datetime import ...` |
| 2 | `F401` | line 8 | `import sys` is unused |
| 3 | `UP035` | line 9 | `from typing import List` is deprecated |
| 4 | `UP006` | line 74 | Return type uses `List[str]` instead of `list[str]` |

# Intentional Unit Test Bugs

The following 4 bugs were introduced across 2 files to be caught by the unit tests:

| # | File | Bug | Failing test(s) |
|---|------|-----|-----------------|
| 1 | `vibe/core/utils/merge.py:59` | `_replace` returns `base` instead of `override` | `test_override_wins`, `test_override_can_be_falsy` |
| 2 | `vibe/core/utils/merge.py:69` | `_concat` returns `override + base` instead of `base + override` | `test_lists_concatenated` |
| 3 | `vibe/core/utils/merge.py:98` | `_merge` uses `{**override, **base}` instead of `{**base, **override}` | `test_dicts_merged_one_level`, `test_nested_dicts_not_recursed` |
| 4 | `vibe/core/utils/retry.py:12` | `500` removed from retryable HTTP status codes | `test_retryable_codes[500]` |

# Intentional Pyright Errors

The following 4 errors were introduced across 2 files to be caught by `uv run pyright`:

| # | Rule | File | Description |
|---|------|------|-------------|
| 1 | `reportAssignmentType` | `vibe/core/utils/slug.py:110` | `_count: str = len(_ADJECTIVES)` — `int` assigned to `str` variable |
| 2 | `reportReturnType` | `vibe/core/utils/slug.py:116` | `create_slug() -> int` but returns a `str` f-string |
| 3 | `reportAssignmentType` | `vibe/core/utils/time.py:6` | `_stamp: int = datetime.now(UTC)` — `datetime` assigned to `int` variable |
| 4 | `reportReturnType` | `vibe/core/utils/time.py:10` | `utc_now() -> str` but returns a `datetime` |
