<!--
# Linear-Optimization
Visualizing some concepts of linear programming problems! <br>
Made by [Amirhossein Sorour](https://github.com/amirhosseinsorour), [Aylar Sedaei](https://github.com/AylarSedaei) <br>
Special Thanks to [Matin Tavakoli](https://github.com/MatinTavakoli), [Hossein Zaredar](https://github.com/HosseinZaredar) <br>

## Videos:
1. [Solving Linear Programming Problems by Graphical Method](https://youtu.be/pATJqDh1v2M)
<img width="750" alt="Thumbnail" src="https://user-images.githubusercontent.com/46843953/171987607-3c6c984c-713a-4603-9709-95c6ea0d8e4a.png">

-->
# Linear Optimization: The Graphical Method

An educational animation that explains how to solve a two-variable linear programming problem using Python and Manim. It connects the algebra of constraints and an objective function to their geometric interpretation.

**[Watch the animation](https://youtu.be/pATJqDh1v2M)** · **[View the Python scene](LinearProgramming.py)**

<img width="750" alt="Preview of the graphical method for linear programming" src="https://user-images.githubusercontent.com/46843953/171987607-3c6c984c-713a-4603-9709-95c6ea0d8e4a.png">

## What the animation explains

- Representing linear constraints as lines and shaded half-planes.
- Combining constraints to construct the feasible region.
- Moving an objective-function line across the feasible region.
- Evaluating corner points and identifying an optimal solution.

## Worked example

The scene maximizes:

$$
z = x_1 + 5x_2
$$

subject to:

$$
6x_1 + 5x_2 \leq 60, \qquad
x_1 + 2x_2 \leq 14, \qquad
x_1 \leq 9, \qquad
x_1, x_2 \geq 0.
$$

The five vertices of the feasible region give the following objective values:

| Vertex | Objective value |
| --- | --- |
| $(0, 0)$ | $0$ |
| $(9, 0)$ | $9$ |
| $(9, 6/5)$ | $15$ |
| $(50/7, 24/7)$ | $170/7$ |
| $(0, 7)$ | $35$ |

The optimal solution is $x_1^* = 0$, $x_2^* = 7$, with $z^* = 35$.

## Repository contents

| Path | Purpose |
| --- | --- |
| [LinearProgramming.py](LinearProgramming.py) | Constraint and objective helpers, plus the `GraphicalMethod` animation scene. |
| [GraphicalMethod.mp4](media/videos/LinearProgramming/1080p60/GraphicalMethod.mp4) | Committed render of the animation. |
| `media/Tex/` | Generated LaTeX assets from rendering. |

## Rendering the scene

The source imports Manim and uses `Tex` to typeset formulas. Rendering requires a compatible Python/Manim environment and a working LaTeX toolchain. Follow the [Manim installation documentation](https://docs.manim.community/en/stable/installation.html) to prepare that environment.

From the repository directory, with the Manim environment active:

```bash
manim -pql LinearProgramming.py GraphicalMethod
```

This follows the command structure in the [Manim quickstart](https://docs.manim.community/en/stable/tutorials/quickstart.html); `-pql` requests a low-quality render with preview.

The original dependency versions are not recorded in this repository, so compatibility with a fresh Manim installation still needs to be checked. The committed MP4 provides the existing rendered result.

## Adapting the example

The constraints, displayed equations, feasible-region vertices, and objective values are defined in the source. To visualize a different problem, update these together so the geometry and labels remain consistent.

## Authors and acknowledgments

Created by [Amirhossein Sorour](https://github.com/amirhosseinsorour) and [Aylar Sedaei](https://github.com/AylarSedaei).

Special thanks to [Matin Tavakoli](https://github.com/MatinTavakoli) and [Hossein Zaredar](https://github.com/HosseinZaredar).
