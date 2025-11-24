# Lec 22- TYPED SOLUTION-PDEs-Finite Element Applications in Two Dimensions

## Study Notes

[Text API failed]

---

## Raw Slide Summaries

### Slide 1

The image presents a slide with the following content:

*   **Course Information**
    *   Course: Numerical Methods
    *   Instructor: Homeyra Pourmohammadali
*   **Title**
    *   Finite Element Application in Two-Dimension

The slide has a white background and features black text for the course information and a blue title. A thin black line separates the course information from the title.

There are no equations, formulas, definitions, bullet points, diagrams, or images on this slide. The content is limited to the course information and title.

### Slide 2

The image displays a slide from a presentation on Learning Outcomes. The slide has a white background with black text and a blue line underneath the title.

*   **Title**
    *   The title of the slide is "Learning Outcomes" in large blue text.
*   **Subtitle**
    *   Below the title, there is a subtitle that reads: "By the end of this lecture, you will be able to:" in smaller black text.
*   **List of Learning Outcomes**
    *   There are three numbered points:
        1.  Formulate the matrix equation for 2D problems using the finite element method.
        2.  Recognize the importance of system topology and effectively number nodes and elements in finite element analysis.
        3.  Evaluate 2D planar trusses using the finite element method.
*   **Slide Number**
    *   In the bottom-right corner, there is a small number "2" indicating that this is the second slide.

The slide outlines the learning objectives for a lecture on finite element methods, specifically focusing on 2D problems and planar trusses.

### Slide 3

The slide, titled "Two-Dimensional Problems," presents a comprehensive overview of the challenges and approaches involved in solving two-dimensional problems using the finite element method. The slide is divided into two main sections: a bulleted list on the left and a graph on the right.

**Bulleted List:**

* The mathematical calculations increase significantly.
* The procedures of the finite element approach in two dimensions are very similar to one-dimensional applications conceptually.

**Graph:**

The graph, labeled "Solution of Poisson's Equation on a square mesh," displays a square mesh with a color gradient that transitions from blue (low values) to red (high values). The mesh consists of a grid of triangles, with a central region of high values (red) surrounded by a gradual decrease in values towards the edges (blue). The x and y axes are labeled with values ranging from 0 to 1, and a vertical color bar on the right side of the graph provides a scale for the color gradient.

**Additional Information:**

A URL is provided below the graph: https://www.particleincell.com/2012/matlab-fem/. The slide number, "3," is displayed in the bottom-right corner.

Overall, the slide effectively conveys the key points and visual representation of solving two-dimensional problems using the finite element method, specifically highlighting the increased complexity of mathematical calculations and the conceptual similarities to one-dimensional applications.

### Slide 4

The slide is titled **Triangular Element** and contains the following content:

**Element Equation**

The equation for the element is:

$u(x,y) = a_0 + a_{1,1}x + a_{1,2}y$

**Condition for the Equation**

The equation should pass through triangle nodes:

* $u_1(x,y) = a_0 + a_{1,1}x_1 + a_{1,2}y_1$
* $u_2(x,y) = a_0 + a_{1,1}x_2 + a_{1,2}y_2$
* $u_3(x,y) = a_0 + a_{1,1}x_3 + a_{1,2}y_3$

**Matrix Form**

The equations can be represented in matrix form as:

$\begin{bmatrix}
1 & x_1 & y_1 \\
1 & x_2 & y_2 \\
1 & x_3 & y_3 \\
\end{bmatrix} \begin{Bmatrix}
a_0 \\
a_{1,1} \\
a_{1,2} \\
\end{Bmatrix} = \begin{Bmatrix}
u_1 \\
u_2 \\
u_3 \\
\end{Bmatrix}$

**Diagram**

The slide also includes a diagram of a triangular element with three nodes labeled 1, 2, and 3. The diagram is a simple line drawing of a triangle with the nodes marked at the vertices. The x and y axes are shown, with the x-axis pointing to the right and the y-axis pointing up. The triangle is drawn on a light blue background with a red border.

### Slide 5

## Triangular Element: Element Equation

### Matrix Equation

The slide presents a matrix equation relating the coefficients $a_0$, $a_{1,1}$, and $a_{1,2}$ to the values $u_1$, $u_2$, and $u_3$:

\[
\begin{bmatrix}
1 & x_1 & y_1 \\
1 & x_2 & y_2 \\
1 & x_3 & y_3 \\
\end{bmatrix}
\begin{Bmatrix}
a_0 \\
a_{1,1} \\
a_{1,2}
\end{Bmatrix}
=
\begin{Bmatrix}
u_1 \\
u_2 \\
u_3
\end{Bmatrix}
\]

### Solving for Unknowns

The slide provides solutions for $a_0$, $a_{1,1}$, and $a_{1,2}$:

- $a_0 = \frac{1}{2A_e} \left[ u_1 (x_2 y_3 - x_3 y_2) + u_2 (x_3 y_1 - x_1 y_3) + u_3 (x_1 y_2 - x_2 y_1) \right]$
- $a_{1,1} = \frac{1}{2A_e} \left[ u_1 (y_2 - y_3) + u_2 (y_3 - y_1) + u_3 (y_1 - y_2) \right]$
- $a_{1,2} = \frac{1}{2A_e} \left[ u_1 (x_3 - x_2) + u_2 (x_1 - x_3) + u_3 (x_2 - x_1) \right]$

### Area of the Triangle

The area $A_e$ of the triangle is given by:

$A_e = \frac{1}{2} \left[ (x_2 y_3 - x_3 y_2) + (x_3 y_1 - x_1 y_3) + (x_1 y_2 - x_2 y_1) \right]$

### Diagram

The slide includes a diagram of a triangle with vertices labeled 1, 2, and 3. The triangle is shown in a light blue box with a red border. The vertices of the triangle are plotted on a Cartesian coordinate system with $x$ and $y$ axes. The vertex labeled 1 is located at the bottom left, vertex 2 is at the top right, and vertex 3 is at the bottom right. The lines connecting the vertices are black.

### Slide 6

The image presents a comprehensive overview of the element equation, focusing on interpolation functions. The content is divided into two main sections: a series of 3D graphs on the left and a detailed mathematical explanation on the right.

**Left Section: 3D Graphs**

*   The left side features four 3D graphs labeled (a), (b), (c), and (d), each representing a triangular element with nodes.
*   Graph (a) displays a 3D triangular element with nodes labeled $u_1$, $u_2$, and $u_3$, along with axes labeled $x$, $y$, and $u$.
*   Graphs (b), (c), and (d) show the interpolation functions $N_1$, $N_2$, and $N_3$, respectively, with their corresponding 3D triangular elements and axes.

**Right Section: Mathematical Explanation**

*   **Element Equation**
    *   The element equation is given by: $u = N_1 u_1 + N_2 u_2 + N_3 u_3$
*   **Interpolation Functions**
    *   The interpolation functions are defined as:
        *   $N_1=\frac{1}{2 A_{e}}\left[\left(x_{2} y_{3}-x_{3} y_{2}\right)+\left(y_{2}-y_{3}\right) x+\left(x_{3}-x_{2}\right) y\right]$
        *   $N_{2}=\frac{1}{2 A_{e}}\left[\left(x_{3} y_{1}-x_{1} y_{3}\right)+\left(y_{3}-y_{1}\right) x+\left(x_{1}-x_{3}\right) y\right]$
        *   $N_{3}=\frac{1}{2 A_{e}}\left[\left(x_{1} y_{2}-x_{2} y_{1}\right)+\left(y_{1}-y_{2}\right) x+\left(x_{2}-x_{1}\right) y\right]$
*   **Sum of Interpolation Functions**
    *   The sum of the interpolation functions is always 1: $N_{1}+N_{2}+N_{3}=1$

### Slide 7

The image presents a slide from a presentation on the Finite Element Method (FEM), specifically focusing on assembly and boundary conditions. The slide features a diagram illustrating a numbering scheme for FEM approximation of a heated plate.

**Title:** 
The title of the slide is "Assembly and Boundary Conditions" in blue text.

**Diagram:**
The diagram is a light blue square divided into 20 smaller triangles by black lines, with each triangle numbered from 1 to 32 in a white circle. The triangles are arranged in a 4x5 grid, with some numbers outside the triangles on the axes. The x-axis is labeled with numbers 1 to 5, and the y-axis is labeled with numbers 1 to 5.

**Key Points:**
Two bullet points are presented to the right of the diagram:

* The assemble and application of BCs are more complicated for 2D and 3D than 1D.
* Establishment of system topology is very important.

**Additional Text:**
At the bottom of the diagram, the text reads: "Numbering scheme for FEM approximation of the heated plate."

**Background:**
The background of the slide is white, providing a clean and neutral backdrop for the diagram and text. 

**Slide Number:**
The slide number "7" is displayed in the bottom-right corner.

### Slide 8

## Step 1: Detailed Summary of Lecture Slide

The lecture slide is titled "Example 1. 2D Truss – FEM Matrix Equation" in red text.

## Step 2: Written Content

The written content on the slide is as follows:

Consider an element of a truss member that is attached to two nodes, 1 and 2.

- **Local Coordinate** $(x',y')$: 1D, $x'$ along the length of element
- **Global coordinate** $(x,y)$: 2D, is not along the length of element

## Step 3: Diagram Description

The diagram on the slide depicts a 2D coordinate system with a red line representing a truss member element. The element is labeled with nodes 1 and 2 at its ends. The coordinate systems shown are:

- **Global Coordinate**: A standard 2D Cartesian coordinate system with $x$ and $y$ axes, labeled at the bottom and left side, respectively.
- **Local Coordinate**: A 1D coordinate system aligned with the truss member element, with $x'$ along the length of the element and $y'$ perpendicular to it. The $x'$ axis runs from node 1 to node 2.

## Step 4: Axes and Labels

- The global coordinate system has axes labeled $x$ (horizontal) and $y$ (vertical).
- The local coordinate system is aligned with the truss element, with $x'$ along the element and $y'$ perpendicular to it.
- Node 1 is at the lower left end of the truss element, and node 2 is at the upper right end.

## 5: Conclusion

The slide illustrates the difference between local and global coordinate systems in the context of a 2D truss element for Finite Element Method (FEM) analysis.

### Slide 9

The image presents a detailed diagram illustrating the Finite Element Method (FEM) matrix equation for a 2D truss, specifically focusing on the transformation of displacements between local and global coordinate systems.

**Title and Description**

* The title, "Example 1. 2D Truss - FEM Matrix Equation," is prominently displayed in red text at the top of the image.
* Below the title, two lines of black text provide definitions:
	+ $q'_1$, $q'_2$: displacements in the local coordinate system
	+ $q_1$, $q_2$, $q_3$, $q_4$: displacements in the x-y (global) coordinate system

**Diagram**

* The diagram features a red line representing the undeformed element and a blue line representing the deformed element.
* The undeformed element is labeled with:
	+ $q_1$ and $q_2$ at the lower end
	+ $q_2'$ and $q_1'$ along the length
	+ $\theta$ (theta) indicating the angle between the element and the horizontal axis
* The deformed element is labeled with:
	+ $q_3$ and $q_4$ at the upper end
	+ Arrows indicating the direction of displacements $q_2 \sin \theta$ and $q_1 \cos \theta$
* The diagram also includes:
	+ A dotted line connecting the ends of the undeformed and deformed elements
	+ Arrows pointing to the displacements $q_2'$ and $q_1'$

**Key Features**

* The diagram illustrates the transformation of displacements from the local coordinate system to the global coordinate system.
* The use of red and blue lines effectively distinguishes between the undeformed and deformed elements.
* The inclusion of labels and arrows provides a clear understanding of the displacements and their relationships.

**Page Number**

* The page number "9" is displayed in small black text at the bottom-right corner of the image.

### Slide 10

The image presents a slide from a presentation on the Finite Element Method (FEM), specifically focusing on a 2D truss example. The title, "Example 1. 2D Truss - FEM Matrix Equation," is prominently displayed in red text at the top of the slide.

**Key Equations and Definitions**

The slide begins by explaining that for small deformations in tension or compression, a beam acts like a spring, and provides two key equations:

*   $F = k\Delta x$
*   $k = \frac{AE}{L}$

The variables are then defined as:

*   $k$: the element stiffness
*   $A$: the cross-sectional area of the element
*   $E$: Young's modulus for the material
*   $L$: the length of the element

**Energy Computation**

The slide then explains how to compute the energy by integrating over the deformation:

*   $u = k \int_{0}^{Q} x dx = \frac{1}{2} kQ^2$

The variable $Q$ is defined as:

*   $Q$: total change in length of the element

**Visual Content**

The slide features a clean and simple design, with a white background and black text. The title and equation variables are highlighted in red and blue, respectively. A small number "10" is located in the bottom-right corner of the slide, likely indicating the slide number.

Overall, the slide provides a clear and concise overview of the key concepts and equations related to the FEM matrix equation for a 2D truss example.

### Slide 11

The image presents a slide from a lecture on the Finite Element Method (FEM), specifically focusing on a 2D truss example. The title, "Example 1. 2D Truss - FEM Matrix Equation," is prominently displayed in red text at the top.

**Key Concepts and Equations:**

* **Q: total change in length of the element**: $Q = (q_2' - q_1')$
* **Assumption:** The deformation is linear over the element. All equal length segments of the element will deform the same amount. This is called a constant strain deformation of the element.
* **Strain Energy Equations:**
	+ $u = \frac{1}{2} k(q_2' - q_1')^2$
	+ $u = \frac{1}{2} k(q_2'^2 - 2q_2'q_1' + q_1'^2)$

**Representation in Matrix Form:**

* **Displacement Vector:** $q' = \begin{Bmatrix} q_1' \\ q_2' \end{Bmatrix}$
* **Stiffness Matrix:** $k' = \frac{AE}{L} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$
* **Strain Energy in Matrix Form:** $u = \frac{1}{2} q'^T k' q'$

**Additional Information:**

* The stiffness matrix $k'$ is labeled as the "1D Stiffness matrix of one element."
* The slide number "11" is displayed in the bottom-right corner.

Overall, this slide provides a detailed example of how to apply the Finite Element Method to a 2D truss problem, including the assumptions, equations, and matrix representation.

### Slide 12

The slide presents a detailed example of a 2D truss using the Finite Element Method (FEM) matrix equation, specifically focusing on the creation of a 2D stiffness matrix.

**Title and Subtitle**
The title of the slide is "Example 1. 2D Truss - FEM Matrix Equation" in red text. The subtitle is "2D Stiffness Matrix Creation:" in purple text.

**Equations and Formulas**
The slide provides several equations and formulas:

* $q' = \begin{Bmatrix} q_1' \\ q_2' \end{Bmatrix}$ and $q = \begin{Bmatrix} q_1 \\ q_2 \\ q_3 \\ q_4 \end{Bmatrix}$
* Transformation equations:
	+ $q_1' = q_1 \cos \theta + q_2 \sin \theta$
	+ $q_2' = q_3 \cos \theta + q_4 \sin \theta$
* $c = \cos \theta$, and $s = \sin \theta$
* $q' = Mq$, where $M = \begin{bmatrix} c & s & 0 & 0 \\ 0 & 0 & c & s \end{bmatrix}$
* $u = \frac{1}{2} q'^T k' q'$
* $u = \frac{1}{2} q^T [M^T k' M] q$

**Diagram**
The slide features a diagram illustrating an un-deformed and deformed element of a 2D truss. The diagram shows:

* A red line representing the un-deformed element
* A blue line representing the deformed element
* Arrows indicating the displacements $q_1$, $q_2$, $q_3$, and $q_4$
* Angles and labels:
	+ $\theta$ (angle between the x-axis and the element)
	+ $q_1 \cos \theta$ and $q_2 \sin \theta$ (components of the displacement $q_1'$)
	+ $q_2'$ (displacement in the local coordinate system)

**Page Number**
The slide is labeled with the page number "12" in the bottom-right corner.

### Slide 13

The image presents a slide from a presentation on the Finite Element Method (FEM) for a 2D truss, focusing on matrix equations. The title, "Example 1. 2D Truss - FEM Matrix Equation," is prominently displayed at the top in red text.

**Section 1: 2D Stiffness Matrix Creation**

* The section is titled "2D Stiffness Matrix Creation:" in purple text.
* Three equations are provided:
	+ $k = M^T k' M$
	+ $M = \begin{bmatrix} c & s & 0 & 0 \\ 0 & 0 & c & s \end{bmatrix}$
	+ $u = \frac{1}{2} q'^T k' q'$, $u = \frac{1}{2} q^T [M^T k' M] q$
* The variables $c$ and $s$ are defined as:
	+ $c = \cos \theta$
	+ $s = \sin \theta$

**Section 2: Stiffness Matrix**

* The stiffness matrix $k$ for global two-dimensional coordinates is given by:
	+ $k = \frac{AE}{L} \begin{bmatrix} c^2 & cs & -c^2 & -cs \\ cs & s^2 & -cs & -s^2 \\ -c^2 & -cs & c^2 & cs \\ -cs & -s^2 & cs & s^2 \end{bmatrix}$

**Additional Information**

* The number "13" is displayed in the bottom-right corner of the slide, likely indicating the slide number.

Overall, the slide provides a detailed explanation of the stiffness matrix creation and its application in the context of a 2D truss using the Finite Element Method.

### Slide 14

The image presents a slide from a presentation on the Finite Element Method (FEM) for a 2D truss, focusing on stress calculations and matrix representation. The title, "Example 1. 2D Truss - FEM Matrix Equation," is prominently displayed in red text at the top.

**Stress Calculations:**

* The stress calculation is represented by two equations:
	+ $\sigma = E \epsilon$
	+ $\sigma = E \frac{q_2' - q_1'}{L}$

A diagram illustrates the concept of total deformation and length of an element, with two black arrows pointing to these labels.

**Matrix Representation:**

* The matrix representation section provides several equations:
	+ $\sigma=\frac{E}{L}\{-1 \quad 1\}\begin{Bmatrix} q_1' \\ q_2' \end{Bmatrix}$
	+ $q' = \begin{Bmatrix} q_1' \\ q_2' \end{Bmatrix}$
	+ $q' = Mq$
	+ $\sigma=\frac{E}{L}\{-1 \quad 1\}Mq$
	+ $\sigma = \frac{E}{L}\{-c \quad -s \quad c \quad s\}q$

**Footer:**

* The footer features blue text that reads, "End of Example 1."
* In the bottom-right corner, the number "14" is displayed.

Overall, the slide provides a detailed explanation of stress calculations and matrix representation for a 2D truss using the Finite Element Method.

### Slide 15

The image presents a detailed diagram of a 2D truss, accompanied by a title and explanatory text. The title, "Example 2. 2D Truss - FEM Analysis," is prominently displayed in red text at the top of the image.

**Title and Text**

*   Title: "Example 2. 2D Truss - FEM Analysis" in red text
*   Subtitle: "Calculate displacement and stress in each element of the following truss under the applied loads shown:" in black text

**Diagram**

*   A 2D truss diagram with various components:
    *   Nodes: 1, 2, 3, 4
    *   Elements: 1, 2, 3, 4
    *   Arrows indicating forces and displacements:
        *   $q_1$, $q_2$, $q_3$, $q_4$, $q_5$, $q_6$, $q_7$, $q_8$
    *   Dimensions:
        *   40" (horizontal distance between nodes 1 and 2)
        *   30" (vertical distance between nodes 1 and 4)
    *   Applied loads:
        *   20,000 lbs (horizontal force at node 2)
        *   25,000 lbs (vertical force at node 3)

**Material Properties**

*   $E = 29.5 \times 10^6$
*   Area $= 1.0$ in$^2$

**Background**

*   White background

Overall, the image provides a clear and detailed representation of a 2D truss problem, including the diagram, material properties, and applied loads.

### Slide 16

The image presents a detailed analysis of a 2D truss using the Finite Element Method (FEM). The truss consists of 4 nodes and 4 elements, with joints constrained to move in x or y directions only.

**Coordinates of Nodes:**

| Node | X | Y |
| --- | --- | --- |
| 1    | 0 | 0 |
| 2    | 40 | 0 |
| 3    | 40 | 30 |
| 4    | 0  | 30 |

**Elements and the nodes they connect in the truss:**

| Element | From Node | To Node |
| --- | --- | --- |
| 1       | 1        | 2      |
| 2       | 3        | 2      |
| 3       | 1        | 3      |
| 4       | 4        | 3      |

**Diagram Description:**

The diagram depicts the truss with nodes labeled 1 to 4 and elements labeled 1 to 4. The nodes are represented by circles, and the elements are represented by lines connecting the nodes. The diagram also shows the following:

*   External forces:
    *   A downward force of 25,000 lbs at node 3
    *   A horizontal force of 20,000 lbs at node 2
*   Reaction forces:
    *   A vertical force labeled q2 at node 1
    *   A horizontal force labeled q1 at node 1
    *   A horizontal force labeled q3 at node 2
    *   A vertical force labeled q4 at node 2
    *   A horizontal force labeled q5 at node 4
    *   A vertical force labeled q6 at node 4
    *   A horizontal force labeled q7 at node 3
    *   A vertical force labeled q8 at node 3

**Element Properties:**

| Element | Length | Cosine | Sine |
| --- | --- | --- | --- |
| 1    | 40    | 1     | 0   |
| 2    | 30    | 0     | -1  |
| 3    | 50    | 0.8   | 0.6 |
| 4    | 40    | 1     | 0   |

**Additional Information:**

*   E = 29.5 x 10^6
*   Area = 1.0 in^2

The image provides a comprehensive overview of the 2D truss analysis using FEM, including node coordinates, element connections, external forces, and element properties.

### Slide 17

The image presents a detailed analysis of a 2D truss using the Finite Element Method (FEM). The content is organized into sections, each addressing a specific aspect of the analysis.

**Example 2. 2D Truss - FEM Analysis**

*   **Stiffness Matrix:**
    *   The stiffness matrix \(k\) is given by the formula:
        \[ k = \frac{AE}{L} \begin{bmatrix} c^2 & cs & -c^2 & -cs \\ cs & s^2 & -cs & -s^2 \\ -c^2 & -cs & c^2 & cs \\ -cs & -s^2 & cs & s^2 \end{bmatrix} \]
    *   Where:
        *   \(A\) = Area = 1.0 in\(^2\)
        *   \(E\) = 29.5 \(\times 10^6\)
        *   \(L\) = length of the element (not explicitly given but implied to be 40 inches for Element 1)
*   **Truss Diagram:**
    *   A 2D truss diagram is provided with the following details:
        *   The truss has four nodes labeled 1, 2, 3, and 4.
        *   The elements are numbered 1, 2, 3, and 4.
        *   External forces are applied:
            *   25,000 lbs downward at node 3.
            *   20,000 lbs to the right at node 2.
        *   Supports:
            *   Node 1 is fixed (no movement in either direction).
            *   Node 2 has a roller support (movement allowed horizontally).
    *   The dimensions of the truss are:
        *   Horizontal span = 40 inches.
        *   Vertical height = 30 inches.
*   **Element 1:**
    *   For Element 1, the stiffness matrix \(k_1\) is calculated as:
        \[ k_1 = \frac{29.5 \times 10^6}{40} \begin{bmatrix} 1 & 0 & -1 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \]
    *   The degrees of freedom (DOF) for the global system are indicated, showing how the local DOF of each element are mapped to the global DOF.

In summary, the image provides a comprehensive overview of applying FEM to a 2D truss, including the formulation of the stiffness matrix, the geometric and loading details of the truss, and the calculation of the stiffness matrix for Element 1.

### Slide 18

The image presents a detailed example of a 2D truss Finite Element Method (FEM) analysis, specifically focusing on the stiffness matrix for elements 2, 3, and 4.

**Title and Subtitle**

* The title, "Example 2. 2D Truss - FEM Analysis," is prominently displayed in red text at the top of the image.
* Below the title, the subtitle "Stiffness Matrix:" is written in purple text.

**Element Stiffness Matrices**

The image presents three element stiffness matrices, each with its own set of equations and formulas:

* **Element 2:**
	+ The equation for the stiffness matrix is: $k_2 = \frac{29.5 \times 10^6}{30} \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & -1 & 0 & 1 \end{bmatrix}_{5 6 3 4}^{5 6 3 4}$
	+ The matrix has a dimension of 4x4, with the following values:
		- Row 1: 0, 0, 0, 0
		- Row 2: 0, 1, 0, -1
		- Row 3: 0, 0, 0, 0
		- Row 4: 0, -1, 0, 1
* **Element 3:**
	+ The equation for the stiffness matrix is: $k_3 = \frac{29.5 \times 10^6}{50} \begin{bmatrix} .64 & .48 & -.64 & -.48 \\ .48 & .36 & -.48 & -.36 \\ -.64 & -.48 & .64 & .48 \\ -.48 & -.36 & .48 & .36 \end{bmatrix}_{1 2 5 6}^{1 2 5 6}$
	+ The matrix has a dimension of 4x4, with the following values:
		- Row 1: 0.64, 0.48, -0.64, -0.48
		- Row 2: 0.48, 0.36, -0.48, -0.36
		- Row 3: -0.64, -0.48, 0.64, 0.48
		- Row 4: -0.48, -0.36, 0.48, 0.36
* **Element 4:**
	+ The equation for the stiffness matrix is: $k_4 = \frac{29.5 \times 10^6}{40} \begin{bmatrix} 1 & 0 & -1 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}_{7 8 5 6}^{7 8 5 6}$
	+ The matrix has a dimension of 4x4, with the following values:
		- Row 1: 1, 0, -1, 0
		- Row 2: 0, 0, 0, 0
		- Row 3: -1, 0, 1, 0
		- Row 4: 0, 0, 0, 0

**Additional Information**

* The background of the image is white.
* In the bottom-right corner, the number "18" is displayed in small gray text.

### Slide 19

The image presents a lecture slide titled "Example 2. 2D Truss - FEM Analysis" in red text at the top. Below the title, in purple text, is the subtitle "Assembled Structural/ Global Stiffness Matrix:".

The main content of the slide is a large matrix, labeled as $K$, which represents the assembled structural or global stiffness matrix. The matrix is given by the equation:

$K = \frac{29.5 \times 10^6}{600}$

The matrix $K$ is an $8 \times 8$ matrix, with rows and columns labeled from 1 to 8. The matrix contains various numerical values, including:

*   $22.68, 5.76, -15.0, 0, -7.68, -5.76, 0, 0$
*   $5.76, 4.32, 0, 0, -5.76, -4.32, 0, 0$
*   $-15.0, 0, 15.0, 0, 0, 0, 0, 0$
*   $0, 0, 0, 20.0, 0, -20.0, 0, 0$
*   $-7.68, -5.76, 0, 0, 22.68, 5.76, -15.0, 0$
*   $-5.76, 4.32, 0, -20.0, 5.76, 24.32, 0, 0$
*   $0, 0, 0, 0, -15.0, 0, 15.0, 0$
*   $0, 0, 0, 0, 0, 0, 0, 0$

In the bottom-right corner of the slide, the number "19" is displayed in small gray text. The background of the slide is white.

### Slide 20

The image presents a detailed diagram and equations for a 2D truss Finite Element Method (FEM) analysis, specifically Example 2. The content is organized into several key components:

**Title and Equation**
The title, "Example 2. 2D Truss - FEM Analysis," is prominently displayed in red text at the top. Below it, the equation \( KQ = F \) is highlighted in a red box, where:
- \( K \) represents the stiffness matrix,
- \( Q \) represents the displacement vector,
- \( F \) represents the force vector.

**Force Vector \( F \)**
The force vector \( F \) is given as:
\[ F = \begin{pmatrix} 0 \\ 0 \\ 20,000 \\ 0 \\ 0 \\ -25,000 \\ 0 \\ 0 \end{pmatrix} \]

**Displacement Vector \( Q \)**
The displacement vector \( Q \) is represented as:
\[ Q = \begin{pmatrix} q_1 \\ q_2 \\ q_3 \\ q_4 \\ q_5 \\ q_6 \\ q_7 \\ q_8 \end{pmatrix} \]

**Truss Diagram**
A diagram of the 2D truss is provided, showing:
- Nodes labeled 1 through 4.
- Elements labeled 1 through 4.
- The truss has a roller support at node 2 and a pin support at node 1.
- External forces are applied:
  - A 20,000 lbs force to the right at node 1.
  - A 25,000 lbs force downwards at node 3.
- Displacements are labeled \( q_1 \) through \( q_8 \) at each degree of freedom.

**Material and Geometric Properties**
Given properties are:
- \( E = 29.5 \times 10^6 \) (modulus of elasticity).
- Area \( = 1.0 \) in\(^2\) (cross-sectional area of the truss elements).

**Dimensions**
The truss dimensions are:
- 40 inches in the horizontal direction (along the bottom).
- 30 inches in the vertical direction (height).

This detailed setup is used for analyzing the behavior of the truss under the applied loads using the Finite Element Method.

### Slide 21

The image presents a lecture slide titled "Example 2. 2D Truss - FEM Analysis" in red text at the top. The main content of the slide is as follows:

**Representation of Global Equation in Matrix Form:**

The equation is represented as:

$\frac{29.5 \times 10^6}{600} \begin{bmatrix}
22.68 & 5.76 & -15.0 & 0 & -7.68 & -5.76 & 0 & 0 \\
5.76 & 4.32 & 0 & 0 & -5.76 & -4.32 & 0 & 0 \\
-15.0 & 0 & 15.0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 20.0 & 0 & -20.0 & 0 & 0 \\
-7.68 & -5.76 & 0 & 0 & 22.68 & 5.76 & -15.0 & 0 \\
-5.76 & 4.32 & 0 & -20.0 & 5.76 & 24.32 & 0 & 0 \\
0 & 0 & 0 & 0 & -15.0 & 0 & 15.0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{bmatrix} \begin{Bmatrix}
q_1 \\
q_2 \\
q_3 \\
q_4 \\
q_5 \\
q_6 \\
q_7 \\
q_8 \\
\end{Bmatrix} = \begin{Bmatrix}
0 \\
0 \\
20,000 \\
0 \\
0 \\
-25,000 \\
0 \\
0 \\
\end{Bmatrix}$

The slide appears to be from a presentation on Finite Element Method (FEM) analysis, specifically focusing on a 2D truss example. The equation represents the global stiffness matrix $K$ multiplied by the displacement vector $Q$, equated to the force vector $F$. The numbers in the matrices and vectors are likely specific to the problem being analyzed. 

There are no diagrams or images on this slide, only mathematical representations. The slide number "21" is displayed in the bottom-right corner.

### Slide 22

## Example 2. 2D Truss - FEM Analysis

### Boundary Conditions:

BC at the fixed supports: joints will not move in the constrained direction. We remove these from our matrix. The lines in equation show the rows and columns that are removed.

### Matrix Equation

The following matrix equation is presented:

$\frac{29.5 \times 10^6}{600} \begin{bmatrix} 22.68 & -5.76 & -15.0 & 0 & -7.68 & -5.76 & 0 & 0 \\ -5.76 & 4.32 & 0 & 0 & -5.76 & -4.32 & 0 & 0 \\ -15.0 & 0 & 15.0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 20.0 & 0 & -20.0 & 0 & 0 \\ -7.68 & -5.76 & 0 & 0 & 22.68 & 5.76 & -15.0 & 0 \\ -5.76 & 4.32 & 0 & -20.0 & 5.76 & 24.32 & 0 & 0 \\ 0 & 0 & 0 & 0 & -15.0 & 0 & 15.0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} \begin{Bmatrix} q_1 \\ q_2 \\ q_3 \\ q_4 \\ q_5 \\ q_6 \\ q_7 \\ q_8 \end{Bmatrix} = \begin{Bmatrix} 0 \\ 0 \\ 20,000 \\ 0 \\ 0 \\ -25,000 \\ 0 \\ 0 \end{Bmatrix}$

### Slide 23

The image presents a detailed slide from a lecture on Finite Element Method (FEM) analysis, specifically focusing on a 2D truss example. The content is organized into sections, each addressing a particular aspect of the analysis.

**Title and Subtitle:**
- **Title:** "Example 2. 2D Truss - FEM Analysis" in red text.
- **Subtitle:** "Boundary Conditions: Simplified equation:" in purple text.

**Equation:**
The slide features a simplified equation related to boundary conditions in FEM analysis:

\[
\frac{29.5 \times 10^6}{600} \begin{bmatrix}
15 & 0 & 0 \\
0 & 22.68 & 5.76 \\
0 & 5.76 & 24.32
\end{bmatrix} \begin{Bmatrix}
q_3 \\
q_5 \\
q_6
\end{Bmatrix} = \begin{Bmatrix}
20,000 \\
0 \\
-25,000
\end{Bmatrix}
\]

**Solution Techniques:**
A brief description mentions that one can use Gaussian elimination or any number of other solution techniques to solve the system of equations.

**Results:**
The results of solving the system of equations are provided as:

\[
\begin{Bmatrix}
q_3 \\
q_5 \\
q_6
\end{Bmatrix} = \begin{Bmatrix}
27.12 \times 10^{-3} \\
5.65 \times 10^{-3} \\
-22.25 \times 10^{-3}
\end{Bmatrix} \text{ inches}
\]

**Slide Number:**
In the bottom-right corner, the slide number "23" is displayed.

**Summary:**
This slide provides a specific example of applying FEM to a 2D truss, including the setup of the equation based on boundary conditions, the method for solving the equation, and the resulting displacements ($q_3$, $q_5$, $q_6$) in inches. There are no diagrams or images on this slide, only text and mathematical equations.

### Slide 24

The slide, titled "Example 2. 2D Truss - FEM Analysis" in red text at the top, presents a detailed analysis of stress calculations for a 2D truss using the Finite Element Method (FEM). 

**Stress Calculation Formula:**
The general formula for stress calculation is provided as:
\[
\sigma = \frac{E}{L} \{-c \quad -s \quad c \quad s\}q
\]
where:
- \(\sigma\) is the stress,
- \(E\) is the modulus of elasticity,
- \(L\) is the length of the element,
- \(c\) and \(s\) are the cosine and sine of the angle of the element, respectively,
- \(q\) is the displacement vector.

**Specific Stress Calculations:**

Two specific stress calculations are shown:

1. **For \(\sigma_1\):**
   \[
   \sigma_{1}=\frac{29.5 \times 10^6}{40}\{-1 \quad 0 \quad 1 \quad 0\}\begin{Bmatrix} 0 \\ 0 \\ 27.12 \times 10^{-3} \\ 0 \end{Bmatrix} \quad \sigma_1 = 20,000 psi
   \]

2. **For \(\sigma_2\):**
   \[
   \sigma_{2}=\frac{29.5 \times 10^6}{30}\{0 \quad 1 \quad 0 \quad -1\}\begin{Bmatrix} -5.65 \times 10^{-3} \\ -22.25 \times 10^{-3} \\ -27.12 \times 10^{-3} \\ 0 \end{Bmatrix} \quad \sigma_2 = -21,875 psi
   \]

**Additional Stress Values:**
Using a similar technique, additional stress values are obtained:
- \(\sigma_3 = -5,208 psi\)
- \(\sigma_4 = 4,167 psi\)

**Slide Details:**
The slide number "24" is displayed in the bottom-right corner, indicating this is part of a larger presentation. The content is presented on a white background with red, purple, and black text. There are no diagrams or images on this slide, only mathematical equations and text.

### Slide 25

## You Try 1. 2D Truss - FEM Analysis

### Problem Statement
A horizontal force $P=1000 kN$ is applied at point $2$ on a planar $2D$ truss (as shown) which is supported by a pin (hinge) joint at point $1$ and two roller supports at point $2$ and $3$. The truss members are simple cylindrical bars with Young's modulus of $E = 210 Gpa$.

### Given Data
- Cross-sectional area of member $1$ (between points $1 \& 2$) and member $2$ (between points $2$ and $3$) are $6 \times10 ^{-4} m^{2}$. 
- Third member (between points $1$ and $3$) has cross-sectional area of $6\sqrt{2} \times 10^{-4}m^{2}$.

### Objective
Use finite element method to find the displacements of points $1, 2$ and $3$.

### Diagram Description
The diagram shows a planar $2D$ truss with the following components:
- **Points**: $1, 2, 3$
- **Members**: 
  - Member $1$: Between points $1$ and $2$ (vertical)
  - Member $2$: Between points $2$ and $3$ (horizontal)
  - Member $3$: Between points $1$ and $3$ (diagonal, $45^\circ$ angle with the horizontal)
- **Supports**:
  - Pin (hinge) joint at point $1$
  - Roller supports at points $2$ and $3$
- **Applied Load**:
  - Horizontal force $P = 1000 kN$ applied at point $2$ to the right
- **Dimensions**:
  - Horizontal distance between points $2$ and $3$: $1m$
  - Vertical distance between points $1$ and $2$: $1m$
  - Angle between member $3$ and the horizontal: $45^\circ$

### Slide 26

The image presents a detailed diagram of a 2D truss structure, accompanied by relevant equations and information for Finite Element Method (FEM) analysis.

**Title:** "You Try 1. Solution. 2D Truss - FEM Analysis"

**Given Parameters:**

*   $P = 1000kN$
*   $L = 1m$
*   $E = 210GPa$
*   $A = 6.0 \times 10^{-4}m^2$ (Elements 1 and 2)
*   $A = 6\sqrt{2} \times 10^{-4}m^2$ (Element 3)

**Step 1: Define the Local Coordinates**

The diagram illustrates a 2D truss structure with labeled nodes (1, 2, 3) and elements (1, 2, 3). The local coordinates are defined as follows:

*   Node 1: $u_1$ and $v_1$
*   Node 2: $u_2$ and $v_2$
*   Node 3: $u_3$ and $v_3$

**Truss Structure Diagram:**

The truss structure consists of three elements and three nodes. The nodes are connected by lines representing the elements. The diagram includes the following features:

*   A pin support at Node 1
*   A roller support at Node 2 and Node 3
*   An external force $P$ applied at Node 2
*   Element 1: connects Node 1 and Node 2 (vertical)
*   Element 2: connects Node 1 and Node 3 (diagonal)
*   Element 3: connects Node 2 and Node 3 (horizontal)

The diagram provides a clear visual representation of the truss structure, allowing for the definition of local coordinates and the application of FEM analysis.

### Slide 27

The slide, titled "You Try 1. Solution. 2D Truss - FEM Analysis," presents a detailed analysis of a 2D truss using the Finite Element Method (FEM). The content is organized into two main sections: Element 1 and Stiffness Matrix of First Element.

**Element 1:**

*   The stiffness matrix \( k \) for Element 1 is given by:

    \[ k = \frac{AE}{L} \begin{bmatrix} c^2 & cs & -c^2 & -cs \\ cs & s^2 & -cs & -s^2 \\ -c^2 & -cs & c^2 & cs \\ -cs & -s^2 & cs & s^2 \end{bmatrix} \]

    where:
    *   \( c = \cos \theta \)
    *   \( s = \sin \theta \)
    *   \( l = \cos \theta = \frac{x_2 - x_1}{L} \)
    *   \( m = \sin \theta \)

**Stiffness Matrix of First Element:**

*   The stiffness matrix \([k_1]\) for the first element is:

    \[ [k_1] = \frac{(6 \times 10^4)(210 \times 10^9)}{1} \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & -1 & 0 & 1 \end{bmatrix} \]

*   Given that \( \theta = 90^\circ \), the following trigonometric values are provided:
    *   \( \cos 90 = 0 \)
    *   \( \sin 90 = 1 \)
    *   \( l = 0 \)
    *   \( m = 1 \)

The slide provides a comprehensive view of how to derive and apply the stiffness matrix for a specific element in a 2D truss analysis using FEM, including the substitution of specific values for \( \theta \) to simplify the matrix.

### Slide 28

The image presents a detailed mathematical representation of stiffness matrices for two elements in a 2D truss Finite Element Method (FEM) analysis. The title, "You Try 1. Solution. 2D Truss - FEM Analysis," is prominently displayed at the top.

**Stiffness Matrix of Second Element:**

The stiffness matrix for the second element is given by:

\[ [k_2] = \frac{(6 \times 10^4)(210 \times 10^9)}{1} \begin{bmatrix} 1 & 0 & -1 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \]

Additionally, the following trigonometric values are provided:

*   \(\theta = 0^\circ\)
*   \(\sin 0 = 0\)
*   \(\cos 0 = 1\)
*   \(l = 1\)
*   \(m = 0\)

**Stiffness Matrix of Third Element:**

The stiffness matrix for the third element is:

\[ [k_3] = \frac{(6\sqrt{2} \times 10^4)(210 \times 10^9)}{\sqrt{2}} \begin{bmatrix} 0.5 & 0.5 & -0.5 & -0.5 \\ 0.5 & 0.5 & -0.5 & -0.5 \\ -0.5 & -0.5 & 0.5 & 0.5 \\ -0.5 & 0.5 & 0.5 & 0.5 \end{bmatrix} \]

The corresponding trigonometric values are:

*   \(\theta = 45^\circ\)
*   \(\sin 45 = \frac{\sqrt{2}}{2}\)
*   \(\cos 45 = \frac{\sqrt{2}}{2}\)
*   \(l = \frac{1}{\sqrt{2}}\)
*   \(m = \frac{1}{\sqrt{2}}\)

There are no diagrams or images on this slide; it consists solely of mathematical equations and formulas. The background of the slide is white, providing a clean and clear visual representation of the information. In the bottom-right corner, the number "5" is displayed in small gray text.

### Slide 29

The image presents a detailed slide from a presentation on Finite Element Method (FEM) analysis, specifically focusing on a 2D truss problem. The title, "You Try 1. Solution. 2D Truss - FEM Analysis," is prominently displayed at the top.

**Global Stiffness Matrix:**

* The global stiffness matrix is defined as:
  $AE/L$ is common in all stiffness matrices: $(6 \times 10^{-4})(210 \times 10^9) = 1260 \times 10^5$

**Assembled Stiffness Matrix:**

* The assembled stiffness matrix $[k]$ is expressed as the sum of individual stiffness matrices: $[k] = [k_1] + [k_2] + [k_3]$
* The assembled stiffness matrix $[k]$ is given by:
  $[k] = 1260 \times 10^5 \begin{bmatrix} 0.5 & 0.5 & 0 & 0 & -0.5 & 0.5 \\ 0.5 & 1.5 & 0 & -1 & -0.5 & -0.5 \\ 0 & 0 & 1 & 0 & -1 & 0 \\ 0 & -1 & 0 & 1 & 0 & 0 \\ -0.5 & -0.5 & -1 & 0 & 1.5 & 0.5 \\ -0.5 & -0.5 & 0 & 0 & 0.5 & 0.5 \end{bmatrix}$

**Equation:**

* The equation $[k][u] = [F]$ is presented, where $[u]$ represents the displacement vector and $[F]$ represents the force vector.

**All Forces (External Effects):**

* The force vector $F$ is defined as:
  $F = \begin{bmatrix} F_{1x} \\ F_{1y} \\ F_{2x} \\ F_{2y} \\ F_{3x} \\ F_{3y} \end{bmatrix}$

The slide provides a comprehensive overview of the global stiffness matrix, assembled stiffness matrix, and the relationship between the stiffness matrix, displacement vector, and force vector in the context of a 2D truss problem using FEM analysis.

### Slide 30

The slide presents a detailed solution to a 2D truss problem using the Finite Element Method (FEM) analysis.

**Title:** "You Try 1. Solution. 2D Truss – FEM Analysis"

**Section 1: Apply Boundary Conditions**

* **Joint 1 (Pin Joint):** Vertical and horizontal displacement is zero at joint 1
	+ $u_1 = 0, v_1 = 0$
* **Joint 2 (Roller Support):** No vertical displacement ($v_2 = 0$), but has a horizontal one
* **Joint 3 (Roller Support):** No vertical displacement ($v_3 = 0$), but has a one in the direction of $u_3$

**Boundary Conditions:**

* $u_1 = v_1 = v_2 = v_3 = 0$

**Section 2: Problem Statement**

* We only need to find $u_2$ and $v_2$
* We know $F_{2x} = 1000kN, [K][u] = [F]$
* Where $[k]$ is the stiffness matrix, $[u]$ is displacement, and $[F]$ is external effects

**Equation:**

The equation presented is a matrix equation:

$1260 \times 10^5 \begin{bmatrix} 0.5 & 0.5 & 0 & 0 & -0.5 & 0.5 \\ 0.5 & 1.5 & 0 & -1 & -0.5 & -0.5 \\ 0 & 0 & 1 & 0 & -1 & 0 \\ 0 & -1 & 0 & 1 & 0 & 0 \\ -0.5 & -0.5 & -1 & 0 & 1.5 & 0.5 \\ -0.5 & -0.5 & 0 & 0 & 0.5 & 0.5 \end{bmatrix} \begin{bmatrix} u_1 \\ v_1 \\ u_2 \\ v_2 \\ u_3 \\ v_3 \end{bmatrix} = \begin{bmatrix} F_{1x} \\ F_{1y} \\ F_{2x} \\ F_{2y} \\ F_{3x} \\ F_{3y} \end{bmatrix}$

The matrix equation has 6 rows and 6 columns, representing the stiffness matrix $[K]$, and the displacement vector $[u]$ and force vector $[F]$ are shown with arrows pointing to their respective components. 

There are no diagrams or images on this slide.

### Slide 31

The image presents a detailed solution to a 2D Truss problem using the Finite Element Method (FEM) analysis. The title, "You Try 1. Solution. 2D Truss - FEM Analysis," is prominently displayed in blue text at the top.

**Problem Statement and Initial Conditions**

* The problem states that the values of $u_1$, $v_1$, $v_2$, and $v_3$ are equal to zero.
* Additionally, it is given that $F_{2x} = 10 \times 10^5$, and $10^5$ cancels out from both sides.

**Elimination Steps**

The elimination steps are outlined as follows:

* First row / First column $\rightarrow$ cancel
* Last row / last column $\rightarrow$ cancel
* 2nd row / 2nd column $\rightarrow$ cancel
* 4th row / 4th column $\rightarrow$ cancel

**Remaining Equations**

The remaining equations are:

$$1260 \begin{bmatrix} 1 & -1 \\ -1 & 1.5 \end{bmatrix} \begin{bmatrix} u_2 \\ u_3 \end{bmatrix} = \begin{bmatrix} 10 \\ F_{3x} \end{bmatrix}$$

It is noted that since there are no other external forces, $F_{3x}$ is equal to zero.

**Solving the Equations**

The equations are then solved as follows:

$$\begin{cases} 1260u_2 - 1260u_3 = 10 \\ -1260u_2 + 1890u_3 = 0 \end{cases} \Longleftrightarrow 630u_3 = 10$$

$$u_3 = \frac{1}{63} = 15.87 \times 10^{-3} \text{ m}$$

Substituting $u_3$ into the second equation yields:

$$-1260u_2 + (1890)(15.87 \times 10^{-3}) = 0 \Longrightarrow u_2 = \frac{1890 \times 15.87 \times 10^{-3}}{1260}$$

The background of the image is white, providing a clean and clear visual representation of the solution. Overall, the image provides a step-by-step solution to a 2D Truss problem using FEM analysis.

### Slide 32

The slide contains the following content:

* **Title**: "References" in large blue text at the top center of the slide.
* **Horizontal line**: A thin blue horizontal line separates the title from the rest of the content.
* **Textbook information**: 
	+ "Textbook: Numerical Methods for Engineers, S. Chapra, R. Canale, 7th Ed. 2015." in black text.
* **Part, Chapter, and Section information**:
	+ "Part 8. Partial Differential Equations" in black text with "Part 8" in blue.
	+ "Chapter 31. Finite Element Method" in black text with "Chapter 31" in blue.
	+ "Section 31.3. Two-Dimensional Problems" in black text with "Section 31.3" in blue.
* **Page number**: The number "32" in small black text at the bottom right corner of the slide.

There are no diagrams, images, equations, formulas, or bullet points on this slide. The background of the slide is white.

### Slide 33

The slide is white with black text. The text is centered and reads: 

"The End 
of Lecture"

The font is a serif font, likely a variation of Times New Roman. The text is in two lines, with "The End" on the first line and "of Lecture" on the second line. The text size is large.

In the bottom-right corner of the slide, there is a small number "33" in a lighter gray color and a smaller font size compared to the main text.

There are no diagrams, images, equations, formulas, definitions, or bullet points on this slide.

