# leetcode-manim

A small Manim project for visualizing algorithm concepts with custom scene components.

## Overview

This repository demonstrates a `binary_search` animation using Manim. The main scene is in `scenes/demo.py` and uses custom helper classes in `components/` to render array cells and pointer labels.

## Project structure

- `scenes/demo.py` - main Manim scene for the binary search demo.
- `components/array_cell.py` - custom `ArrayCell` class for rendering numbered squares.
- `components/pointer.py` - custom `Pointer` class for rendering labeled arrows.
- `code/binary_search.py` - example Python code displayed in the animation.
- `main.py` - lightweight Python module entrypoint.
- `pyproject.toml` - project metadata and dependency declaration.

## Requirements

- Python 3.12.13 or newer
- `manim>=0.20.1`

## Getting started

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install Manim:

```powershell
pip install manim>=0.20.1
```

3. Run the demo scene from the project root:

```powershell
manim -pql scenes/demo.py Demo
```

## Notes

- The scene imports `components.array_cell` and `components.pointer` from `scenes/demo.py`.
- The `scenes/demo.py` file adds the project root to `sys.path` so the `components` package can be imported correctly when Manim loads the scene.

## Customization

- Modify `components/array_cell.py` to change the appearance of array cells.
- Modify `components/pointer.py` to change pointer labels or arrow styling.
- Change `code/binary_search.py` to display different code during the animation.
- Add new scenes under `scenes/` and render them with Manim.

## License

This repository is provided as-is for learning and experimentation with Manim.
