# Lec 21-ANNOTATED- PDE-1D FEM examples-Linear Springs-Heated Rod1

## Study Notes

[Text API failed]

---

## Raw Slide Summaries

### Slide 1

The image presents a slide with the following content:

* **Course Information**
	+ Course: Numerical Methods
	+ Instructor: Homeyra Pourmohammadali
* **Title**
	+ Finite-Element Application in One-Dimension

The slide features a simple design with a white background and black text for the course information, accompanied by a thin black line separating the course details from the title. The title itself is displayed in blue text.

There are no equations, formulas, definitions, bullet points, diagrams, or images present on this slide. The content is limited to the course information and title.

### Slide 2

The image presents a slide from a lecture on Finite Element Methods (FEM), titled "Learning Outcomes" in blue text at the top. The slide outlines the expected learning objectives by the end of the lecture.

*   The title is underlined with a thin blue line.
*   The main content is divided into three bullet points:
    *   **Apply FEM to one-dimensional problems, including springs, axial bars, and interconnected systems.**
    *   **Derive and assemble FEM matrix equations, incorporating boundary conditions.**
    *   **Develop finite-element solutions for a heated rod using direct and weighted residual methods.**
*   The background of the slide is white, providing a clean and clear visual presentation.
*   In the bottom-right corner, the number "2" is displayed in small black text, likely indicating the slide number.

Overall, the slide effectively communicates the key learning objectives for the lecture, providing a clear roadmap for students to understand the topics that will be covered.

### Slide 3

The image presents a slide with a title in large, dark blue text against a gradient background that transitions from white at the top to light blue at the bottom.

*   The title is centered and reads:
    *   "Finite-Element Formulation of a"
    *   "Linear (Elastic) Spring"
    *   "Direct Method"

The slide appears to be an introduction to a presentation on the finite-element formulation of a linear elastic spring using the direct method. There are no equations, formulas, definitions, bullet points, diagrams, or images on this slide. The content is limited to the title.

### Slide 4

The image presents a lecture slide focused on the Finite Element Method (FEM) applied to a one-dimensional linear spring problem. The title, "Example 1. FEM. 1D. One Linear Spring," is prominently displayed in red text at the top.

**Problem Statement:**

The problem involves a linear elastic spring with stiffness $k$ connecting two nodes, $i$ and $i+1$. The forces acting on these nodes are denoted as $F_i$ and $F_{i+1}$, respectively. A coordinate system $x$ is defined, with positive direction from left to right (from node $i$ to $i+1$). The objective is to develop a FEM formulation using the direct method to solve for the nodal displacements $x_i$ and $x_{i+1}$.

**Equations and Matrix Formulation:**

The equations are represented in matrix form, including:

* Stiffness matrix $[k]$
* Displacement vector $\{u\}$
* Force vector $\{F\}$

The matrix equation is:

$[k]\{u\} = \{F\}$

**Diagram:**

A diagram illustrates the problem, featuring:

* A horizontal line representing the spring
* Two nodes, $i$ and $i+1$, marked with circles
* Arrows indicating the forces $F_i$ and $F_{i+1}$ acting on the nodes
* A coordinate system $x$ with labeled points $0$, $x_i$, and $x_{i+1}$

**Key Points:**

* The problem is a simple example of applying FEM to a linear spring
* The goal is to solve for nodal displacements using the direct method
* The matrix formulation provides a concise representation of the equations

Overall, the slide provides a clear and concise introduction to applying FEM to a basic problem in mechanics.

### Slide 5

The slide presents an example of a one-dimensional linear spring problem using the Finite Element Method (FEM). The content is as follows:

*   **Title**: Example 1. Solution. FEM. 1D. One Linear Spring
*   **Assumptions and Hook's Law**:
    *   Assume spring is linear, which implies that Hook's Law can be applied to describe the relationship between deformation and spring force.
    *   Hook's Law: Force = Stiffness × Spring deformation (displacement)
    *   F = kx
*   **Stationary System (in equilibrium)**:
    *   For a stationary system in equilibrium, the forces at each node are equal and opposite: Fi = -Fi+1
*   **Element Equations**:
    *   Two equations are derived:
        *   Fi = kxi - kxi+1
        *   Fi+1 = -kxi + kxi+1
*   **Matrix Representation**:
    *   The element equations can be represented in matrix form as:

        \[\begin{bmatrix} k & -k \\ -k & k \end{bmatrix} \begin{bmatrix} x_i \\ x_{i+1} \end{bmatrix} = \begin{bmatrix} F_i \\ F_{i+1} \end{bmatrix}\]
*   **Interpretation**:
    *   This matrix equation specifies the behavior of the element in response to forces.

The slide provides a detailed explanation of how to develop an element equation for a one-dimensional linear spring problem using the Finite Element Method. It covers the assumptions, application of Hook's Law, and the derivation of the matrix representation of the element equations.

### Slide 6

The slide presents an example of a Finite Element Method (FEM) formulation for analyzing the displacement (deformation) of a spring between two nodes.

**Title:** 
Example 1. Solution. FEM. 1D. One Linear Spring

**Equation:**
The equation is presented in a matrix form:

$\begin{bmatrix} k & -k \\ -k & k \end{bmatrix} \begin{Bmatrix} x_i \\ x_{i+1} \end{Bmatrix} = \begin{Bmatrix} F_i \\ F_{i+1} \end{Bmatrix}$

**Matrix Components:**

* $\begin{bmatrix} k & -k \\ -k & k \end{bmatrix}$: **Stiffness matrix**
* $\begin{Bmatrix} x_i \\ x_{i+1} \end{Bmatrix}$: **Column vector of unknowns at the nodes**
* $\begin{Bmatrix} F_i \\ F_{i+1} \end{Bmatrix}$: **Column vector of external forces applied at the nodes**

**Description:** 
Then, this is presenting the FEM formulation of one element for analyzing the displacement (deformation) of a spring between two nodes.

### Slide 7

The image presents a slide from a presentation on the Finite Element Method (FEM), specifically focusing on a one-dimensional linear spring problem. The title of the slide is "You Try 1. FEM. 1D. One Linear Spring."

**Problem Statement:**

The slide poses three questions:

1. Present the FEM matrix equation (general form) for the following linear spring:

   - A diagram illustrates a linear spring with the following characteristics:
     - The spring constant \(k = 10 N/m\).
     - The spring is fixed at point 1 and has a force of \(5N\) applied at point 2.
     - The x-axis is labeled with points 0, \(x_1\), and \(x_2\), representing the positions of points 1 and 2, respectively.

2. One step in the FEM procedure is the application of boundary conditions and modifying the matrix equation. If the spring is fixed at point 1, and a \(5N\) load is only applied at point 2, what are the boundary conditions?

3. How can the modified matrix equation be presented after the application of boundary conditions (BC)?

**Key Elements:**

- The spring constant \(k = 10 N/m\).
- A \(5N\) force applied at point 2.
- Point 1 is fixed.

**Equations and Formulas:**

No specific equations or formulas are provided on the slide, but it implies the use of the general form of the FEM matrix equation, which typically involves the stiffness matrix and the force vector.

**Diagrams and Images:**

- A simple diagram of a linear spring with a force applied at one end and fixed at the other.
- The x-axis is shown with key points labeled.

**Written Text:**

The slide contains explanatory text for the three questions posed, guiding the reader through the process of applying FEM to a simple linear spring problem, including setting up the matrix equation and applying boundary conditions. 

In summary, the slide provides a basic problem setup for applying the Finite Element Method to a linear spring, focusing on formulating the FEM matrix equation and applying boundary conditions.

### Slide 8

The image presents a detailed lecture slide focused on the Finite Element Method (FEM) applied to a one-dimensional linear spring problem. The title, "You Try 1. Solution. FEM. 1D. One Linear Spring," is prominently displayed at the top in blue text.

**Equations and Formulations:**

The slide features several key equations and formulations:

1. **Matrix Equation:** 
   \[
   \begin{bmatrix}
   k & -k \\
   -k & k
   \end{bmatrix}
   \begin{Bmatrix}
   x_1 \\
   x_2
   \end{Bmatrix}
   =
   \begin{Bmatrix}
   f_1 \\
   f_2
   \end{Bmatrix}
   \]
   Substituting \(k = 10\) N/m, it becomes:
   \[
   \begin{bmatrix}
   10 & -10 \\
   -10 & 10
   \end{bmatrix}
   \begin{Bmatrix}
   x_1 \\
   x_2
   \end{Bmatrix}
   =
   \begin{Bmatrix}
   0 \\
   5
   \end{Bmatrix}
   \]

2. **Boundary Conditions (BC):**
   - No force at node 1 (\(f_1 = 0\))
   - No displacement at node 1 (\(x_1 = 0\))

3. **Modified Matrix Equation after Application of BC:**
   \[
   \begin{bmatrix}
   1 & 0 \\
   -10 & 10
   \end{bmatrix}
   \begin{Bmatrix}
   x_1 \\
   x_2
   \end{Bmatrix}
   =
   \begin{Bmatrix}
   0 \\
   5
   \end{Bmatrix}
   \]

**Diagram:**

A simple diagram illustrates a linear spring with the following details:
- The spring constant \(k = 10\) N/m.
- Node 1 is fixed.
- A force of 5 N is applied at node 2.
- The x-axis is labeled, indicating the direction of the force and the displacement.

**Key Points:**

- The problem involves solving for the displacements \(x_1\) and \(x_2\) using the FEM.
- The application of boundary conditions modifies the matrix equation to solve for \(x_2\).
- The solution to the modified matrix equation will provide the displacement at node 2.

Overall, the slide provides a step-by-step approach to solving a simple FEM problem involving a one-dimensional linear spring, including the formulation of the matrix equation, application of boundary conditions, and the modified equation to be solved.

### Slide 9

The image presents a detailed diagram and description of a cylindrical rod under tensile stress, accompanied by a brief text explaining the scenario. The content is organized as follows:

**Title**
- The title, "Example 2. FEM.1D. Stress Analysis of an Axial Bar Element," is prominently displayed in red text at the top of the image.

**Descriptive Text**
- Below the title, a paragraph of black text provides context for the diagram:
  - "Consider a cylindrical rod (bar element) of length $l$ and cross-sectional area of $A$, with a tensile force $F$, applied along the axis in the positive $x$ direction. Develop the FEM formulation using direct method and present it in matrix form."

**Diagram**
- A diagram occupies the central part of the image, illustrating a cylindrical rod with the following features:
  - The rod is depicted in a light orange color with rounded edges.
  - It has a length labeled as $l$ (in green text) and is oriented horizontally.
  - The cross-sectional area at one end is labeled as $A$ (in green text).
  - A tensile force $F$ (in green text) is represented by a green arrow pointing to the right, applied along the axis of the rod.
  - Another green arrow points to the left, suggesting an equal and opposite force at the other end of the rod, though it's not labeled.

**Axes and Labels**
- The diagram includes labels for the length ($l$) and cross-sectional area ($A$), as well as the force ($F$).
- No specific axes (like x, y, z) are drawn, but the direction of the force $F$ is indicated to be along the positive $x$ direction.

**Page Number**
- In the bottom-right corner, the number "9" is displayed in small black text, indicating the page number.

In summary, the image provides a clear and concise visual and textual representation of a cylindrical rod under tensile stress, setting the stage for a stress analysis problem using the Finite Element Method (FEM).

### Slide 10

The image presents a detailed illustration of an axial bar element, accompanied by relevant equations and formulas. The title, "Example 2. Solution. FEM.1D. Axial Bar Element," is prominently displayed in blue text at the top.

**Visual Representation:**

* A cylindrical bar with a peach-colored body and green arrows on either side, indicating the direction of force application.
* The bar is labeled with the following:
	+ $A$ (cross-sectional area) on the right side
	+ $F$ (force) on the right side
	+ $l$ (length) along the bottom

**Equations and Formulas:**

The image features several handwritten equations and formulas in red ink, which are:

* Normal stress: $\sigma = \frac{F}{A}$
* Axial strain: $\epsilon = \frac{\Delta L}{L}$
* Young's modulus: $E = \frac{\sigma}{\epsilon}$
* Derived equations:
	+ $F = \left(\frac{AE}{l}\right) \Delta L$
	+ $F = k \Delta X$ (similar to the equation of a linear spring)
	+ $k = \frac{AE}{l}$

**Key Takeaways:**

The image effectively illustrates the relationship between normal stress, axial strain, and Young's modulus in the context of an axial bar element. The derived equations demonstrate how the force applied to the bar is related to its deformation and material properties. Overall, the image provides a clear and concise visual representation of the key concepts and formulas involved in analyzing axial bar elements.

### Slide 11

The image presents a detailed lecture slide on the Finite Element Method (FEM) for a 1D axial bar element. The slide is titled "Example 2. Solution. FEM.1D. Axial Bar Element" in blue text.

**Main Content**

The slide features a comprehensive list of specifications for the axial bar element, written in red handwriting:

*   **a) Node numbers on the bar element (node 1 and 2)**
*   **b) The applied forces at each node (P1 and P2)**
*   **c) The displacement at " " (u1 and u2)**
*   **d) The local coordinate system (consider the positive direction of u. (positive from left to right))**

**Diagram and Equations**

A diagram illustrates a bar element with two nodes, labeled 1 and 2, and arrows representing the applied forces P1 and P2. The diagram also shows the displacements u1 and u2 at each node.

The following equations are presented:

*   **{P} = [K] {u}**
*   **Similarly:** $\frac{EA}{L} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \begin{Bmatrix} u_1 \\ u_2 \end{Bmatrix} = \begin{Bmatrix} P_1 \\ P_2 \end{Bmatrix}$

The stiffness matrix is highlighted, and the nodal displacement is defined.

**Key Terms**

*   **Stiffness matrix:** $\frac{EA}{L} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$
*   **Nodal displacement:** $\begin{Bmatrix} u_1 \\ u_2 \end{Bmatrix}$
*   **Applied forces:** $\begin{Bmatrix} P_1 \\ P_2 \end{Bmatrix}$

**Page Number**

The slide is labeled with the page number "11" in the bottom-right corner.

### Slide 12

The slide presents a problem for a stress analysis of an axial bar element using the Finite Element Method (FEM). The problem is as follows:

**Problem Statement:**

Consider a bar made of steel with the following properties:

* Young's modulus (E) = 30 × 10^6 psi
* Length (L) = 10 in
* Diameter (D) = 1 in

The bar is fixed at one end and subjected to an axial load of F = 5000 lb at the other end.

**Tasks:**

a) Present the FEM matrix equation for solving the displacement u2.
b) Apply the boundary conditions and determine the displacement u2.
c) Use the value of u2 and calculate the stress in the element using the formula:

σx = Eε = E * (Δl / l) = E * ((u2 - u1) / l)

**Diagram:**

The diagram shows a cylindrical bar with a fixed end on the left and an applied force on the right. The bar has a length of 10 inches and a diameter of 1 inch. The nodes are labeled as 1 (fixed end) and 2 (end with the applied force). The force F = 5000 lb is represented by a green arrow pointing to the right.

**Key Information:**

* The bar is made of steel with E = 30 × 10^6 psi.
* The length of the bar is 10 inches.
* The diameter of the bar is 1 inch.
* The bar is fixed at one end and subjected to an axial load of F = 5000 lb at the other end.

Overall, the slide presents a clear and concise problem for stress analysis of an axial bar element using the Finite Element Method.

### Slide 13

The image shows a lecture slide titled "You Try 2. Solution. FEM.1D. Stress in an Axial Bar Element" in blue text at the top. 

The slide contains handwritten red text and equations, which appear to be a solution to a problem involving the Finite Element Method (FEM) for a 1D axial bar element. The content is divided into three sections labeled "a)", "b)", and "c)".

**Section a)**
This section provides the following information:
- $A = 0.7854 \: in^2$
- $k = \frac{AE}{L} = \frac{(0.7854)(36\times 10^6 \: psi)}{10} = 2.3652 \times 10^6 \: lb/in^2$
- A matrix equation: $(2.3652 \times 10^6) \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \begin{Bmatrix} u_1 \\ u_2 \end{Bmatrix} = \begin{Bmatrix} -5000 \\ 5000 \end{Bmatrix}$ 
- The note "Before Application of BC" is written to the right of the equation.

**Section b)**
This section provides the following information:
- Boundary conditions (BC): $P_1=0$ (it is fixed at node 1) and $u_1=0$ 
- A modified matrix equation: $\begin{bmatrix} 1 & 0 \\ -2.3652 \times 10^6 & 2.3652 \times 10^6 \end{bmatrix} \begin{Bmatrix} u_1 \\ u_2 \end{Bmatrix} = \begin{Bmatrix} 0 \\ 5000 \end{Bmatrix}$ 
- The solution $u_2 = 2.12 \times 10^{-3} \: in$

**Section c)**
This section provides the following information:
- The formula for stress: $\sigma_x = E\epsilon = E \frac{(u_2-u_1)}{L}$
- The calculated stress: $6.3466 \: psi$ with the note "Stress in element".

### Slide 14

The slide presents a problem involving the deformation of a series of linear springs using the Finite Element Method (FEM). The title, "Example 3. FEM.1D. Deformation of Series of Linear Springs," is prominently displayed in red text at the top.

**Problem Statement:**

* Assume a series of interconnected linear springs with the same stiffness of $k=1$ N/m.
* One end is fixed to the wall, while the other is subjected to a constant force $F=1$ N.
* The task is to determine the displacement of the springs using FEM with the direct method.

**Diagram:**

* A simple diagram illustrates the setup, featuring:
	+ A wall on the left side, represented by a black diagonal line pattern.
	+ A series of five springs connected in series, depicted as blue coils.
	+ Four nodes or points connecting the springs, shown as small white circles.
	+ A black arrow pointing to the right, labeled "Force," indicating the direction of the applied force.
* The diagram is positioned below the problem statement, providing a visual representation of the system.

**Key Information:**

* Stiffness of each spring: $k=1$ N/m
* Applied force: $F=1$ N
* The problem is to be solved using the Finite Element Method (FEM) with the direct method.

### Slide 15

The image presents a detailed illustration of a problem involving the deformation of a series of linear springs, specifically focusing on the Finite Element Method (FEM) in one dimension. The title, "Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs," is prominently displayed at the top.

**Step 1: Discretize, specify node numbers, and the designations of the corresponding forces and displacements at the nodes**

*   The first step in solving this problem involves discretizing the system into nodes and elements.
*   The system consists of a series of linear springs connected in line, with one end fixed to a wall and the other end subjected to an external force.
*   The discretization process involves dividing the system into smaller parts, which are referred to as elements and nodes.

**Diagram Description:**

*   A diagram shows a series of springs connected in line, with one end fixed to a wall (represented by diagonal lines) and the other end subjected to an external force (represented by a black arrow pointing to the right).
*   Below the spring diagram, a line with five nodes labeled 1 through 5 is shown, with each node represented by a black dot.
*   The elements are represented by lines connecting the nodes, with each element numbered from 1 to 4.

**Key Points:**

*   Each spring can be considered as one element, resulting in a total of 4 elements and 5 nodes.
*   The nodes are labeled from 1 to 5, and the elements are labeled from 1 to 4.

**Equations and Formulas:**

*   No specific equations or formulas are presented in the image.

**Definitions:**

*   **Node:** A point in the system where the displacement or force is defined.
*   **Element:** A small part of the system, in this case, a single spring.

**Bullet Points:**

*   None are present in the image.

**Written Text:**

*   The title: "Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs"
*   Step 1 description: "Discretize, specify node numbers, and the designations of the corresponding forces and displacements at the nodes"
*   Text below the diagram: "Each spring can be one element → 4 element , 5 nodes"

Overall, the image provides a clear and detailed illustration of the first step in solving a problem involving the deformation of a series of linear springs using the Finite Element Method.

### Slide 16

The image presents a detailed lecture slide focused on the Finite Element Method (FEM) as applied to a series of linear springs. The slide is titled "Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs" and subtitled "Step 2. Develop the equation for each element."

**Key Components:**

* **Diagram:** A simple diagram illustrates two nodes (Node 1 and Node 2) connected by a spring element. The nodes are labeled with their respective displacements, $x_1$ and $x_2$, and forces, $F_1$ and $F_2$. The diagram is accompanied by a simple axis labeled "x" with points marked at $x_1$ and $x_2$.

* **Equations:** The slide features a matrix equation that represents the relationship between the forces and displacements of the spring element:

\[
\begin{bmatrix}
k_{11}^{(e)} & -k_{12}^{(e)} \\
-k_{21}^{(e)} & k_{22}^{(e)}
\end{bmatrix}
\begin{Bmatrix}
x_1 \\
x_2
\end{Bmatrix}
=
\begin{Bmatrix}
F_1^{(e)} \\
F_2^{(e)}
\end{Bmatrix}
\]

* **Annotations:** The slide includes handwritten annotations in red ink:
	+ $(e)$: denotes that those are the element equations.
	+ $k_{ij}$: denotes their location in the $i^{th}$ row and $j^{th}$ column.
	+ Stiffness matrix for the first element is: $\begin{bmatrix} k_{11}^{(1)} & -k_{12}^{(1)} \\ -k_{21}^{(1)} & k_{22}^{(1)} \end{bmatrix}$

**Summary:** The slide provides a detailed explanation of how to develop the equation for each element in a series of linear springs using the Finite Element Method. It includes a diagram illustrating the nodes, displacements, and forces, as well as a matrix equation representing the relationship between these quantities. The handwritten annotations provide additional context and clarification on the notation and terminology used. Overall, the slide appears to be part of a larger lecture on the application of FEM to solve problems involving linear springs.

### Slide 17

The image presents a slide from a presentation on the Finite Element Method (FEM), specifically focusing on the deformation of a series of linear springs. The title, "Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs," is displayed in blue text at the top.

**Step 2: Develop the equation for each element**

The slide outlines the stiffness matrix for each element in the series:

*   **Stiffness matrix for element 1:** $e=1$

    \[\begin{bmatrix} k_{11}^{(1)} & -k_{12}^{(1)} \\ -k_{21}^{(1)} & k_{22}^{(1)} \end{bmatrix}\]
*   **Stiffness matrix for element 2:** $e=2$

    \[\begin{bmatrix} k_{11}^{(2)} & -k_{12}^{(2)} \\ -k_{21}^{(2)} & k_{22}^{(2)} \end{bmatrix}\]
*   **Stiffness matrix for element 3:** $e=3$

    \[\begin{bmatrix} k_{11}^{(3)} & -k_{12}^{(3)} \\ -k_{21}^{(3)} & k_{22}^{(3)} \end{bmatrix}\]
*   **Stiffness matrix for element 4:** $e=4$

    \[\begin{bmatrix} k_{11}^{(4)} & -k_{12}^{(4)} \\ -k_{21}^{(4)} & k_{22}^{(4)} \end{bmatrix}\]

The slide appears to be part of a larger presentation, with the page number "17" visible in the bottom-right corner. The content suggests that this is an educational resource, likely used in a lecture or tutorial on the Finite Element Method.

### Slide 18

The slide presents a detailed breakdown of the steps involved in developing equations for each element in a series of linear springs using the Finite Element Method (FEM). The title at the top reads:

**Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs**

with a subtitle:

**Step 2. Develop the equation for each element**

The slide is divided into four sections, each representing a different element in the series of linear springs. Each section includes:

* A diagram of the element with nodes labeled
* A force vector equation for the element

The elements are numbered from 1 to 4, and each element has two nodes. The diagrams show the nodes as dots connected by a line, with the element number circled.

The force vector equations are presented in the following format:

* **Force vector for element [number], nodes [node1] and [node2]:**
	+ A curly bracket containing two force components, one for each node

The equations are as follows:

* **Force vector for element 1, nodes 1 and 2:**
	+ {F1(1)  F2(1)}
* **Force vector for element 2, nodes 2 and 3:**
	+ {F2(2)  F3(2)}
* **Force vector for element 3, nodes 3 and 4:**
	+ {F3(3)  F4(3)}
* **Force vector for element 4, nodes 4 and 5:**
	+ {F4(4)  F5(4)}

The background of the slide is white, with black text and red handwriting-style annotations. The slide number "18" is located at the bottom right corner. Overall, the slide provides a clear and detailed representation of the force vectors for each element in the series of linear springs.

### Slide 19

The image presents a detailed lecture slide focused on the Finite Element Method (FEM) for analyzing the deformation of a series of linear springs. The slide is titled "Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs" and outlines the steps involved in solving such a problem.

**Step 3: Assembly**

*   The slide highlights **Step 3**, which involves assembling the force vector.
*   The assembled force vector is represented as $\{ F' \}$.

**Equations and Formulas**

*   The slide displays several equations and formulas related to the assembly of the force vector:
    *   $\begin{Bmatrix} F_1^{(1)} \\ F_2^{(1)} \end{Bmatrix} + \begin{Bmatrix} F_2^{(2)} \\ F_3^{(2)} \end{Bmatrix} + \begin{Bmatrix} F_3^{(3)} \\ F_4^{(3)} \end{Bmatrix} + \begin{Bmatrix} F_4^{(4)} \\ F_5^{(4)} \end{Bmatrix}$
    *   $\begin{Bmatrix} F_1^{(1)} \\ F_2^{(1)} + F_2^{(2)} \\ F_3^{(2)} + F_3^{(3)} \\ F_4^{(3)} + F_4^{(4)} \\ F_5^{(4)} \end{Bmatrix} \rightarrow \begin{Bmatrix} F_1^{(1)} \\ 0 \\ 0 \\ 0 \\ F_5^{(4)} \end{Bmatrix} = \{ F' \}$

**Diagram and Image Description**

*   A diagram is presented, illustrating a series of linear springs with nodes and elements labeled.
*   The diagram shows:
    *   Five nodes labeled 1 to 5.
    *   Four elements labeled 1 to 4.
    *   Arrows indicating forces applied at each node.

**Internal Forces Cancellation**

*   The slide notes that internal forces cancel when equations are assembled:
    *   $F_2^{(1)} = -F_2^{(2)}$
    *   $F_3^{(2)} = -F_3^{(3)}$
    *   $F_4^{(3)} = -F_4^{(4)}$

Overall, the slide provides a detailed explanation of the assembly process for the force vector in the context of the Finite Element Method for analyzing the deformation of a series of linear springs.

### Slide 20

The image presents a detailed slide from a lecture on the Finite Element Method (FEM), specifically focusing on the deformation of a series of linear springs. The title, "Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs," is prominently displayed at the top in blue text.

**Step 3: Assembly**

The main content of the slide is organized under the heading "Step 3. Assembly" in purple text, followed by the subheading "Assembled stiffness matrix:" in black text. The assembled stiffness matrix is represented as a large matrix equation, which is the central element of the slide. This equation illustrates the assembly process of the stiffness matrix for a series of linear springs using the Finite Element Method.

The assembled stiffness matrix is shown as:

```
[ k11(1)  -k12(1)  ]   [ k11(2)  -k12(2) ]   [ k11(3)  -k12(3) ]   [ k11(4)  -k12(4) ]
[ -k21(1)  k22(1) ] + [ -k21(2)  k22(2) ] + [ -k21(3)  k22(3) ] + [ -k21(4)  k22(4) ]
```

Each term in the matrix is labeled with a superscript indicating the element number (1, 2, 3, or 4) and a subscript indicating the position within the element's stiffness matrix (11, 12, 21, or 22). The elements are represented by red ovals around their respective stiffness matrices.

**Key Components**

*   The slide features a white background with black text and red handwritten-style annotations.
*   The title and headings are in blue and purple text, respectively.
*   The assembled stiffness matrix is the primary focus, showcasing the combination of individual element stiffness matrices to form the global stiffness matrix.
*   The slide is numbered "20" in small gray text at the bottom right corner.

Overall, this slide provides a detailed illustration of the assembly process in the Finite Element Method for a series of linear springs, highlighting the construction of the global stiffness matrix from individual element matrices.

### Slide 21

The image presents a detailed representation of a lecture slide focused on the Finite Element Method (FEM) as applied to the deformation of a series of linear springs. The title, "Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs," is prominently displayed at the top in blue text.

**Step 3: Assembly**

The slide is specifically addressing Step 3, which involves the assembly process. The section header, "Step 3. Assembly," is written in purple text, followed by the subheading "Assembled stiffness matrix:" in black text.

**Assembled Stiffness Matrix**

The core content of the slide is the assembled stiffness matrix, denoted as \([k]\), which is a large matrix with the following structure:

\[
[k] =
\begin{bmatrix}
k_{11}^{(1)} & -k_{12}^{(1)} & & & & & \\
-k_{21}^{(1)} & k_{22}^{(1)} + k_{11}^{(2)} & -k_{12}^{(2)} & & & & \\
& -k_{21}^{(2)} & k_{22}^{(2)} + k_{11}^{(3)} & -k_{12}^{(3)} & & & \\
& & -k_{21}^{(3)} & k_{22}^{(3)} + k_{11}^{(4)} & -k_{12}^{(4)} & \\
& & & & & & \\
& & & & & & \\
& & & & -k_{21}^{(4)} & k_{22}^{(4)}
\end{bmatrix}
\]

This matrix is written in red handwriting and appears to be a partially filled matrix, with some entries not specified. The matrix represents the assembled stiffness matrix for a system of linear springs, where each spring contributes to the overall stiffness of the system.

**Key Observations**

* The matrix is symmetric, indicating that the system is conservative.
* The diagonal elements represent the sum of the stiffness coefficients of the springs connected to each node.
* The off-diagonal elements represent the negative of the stiffness coefficients of the springs connecting adjacent nodes.

Overall, the slide provides a clear and detailed illustration of the assembly process in the context of the Finite Element Method for analyzing the deformation of a series of linear springs.

### Slide 22

The image presents a lecture slide focused on the Finite Element Method (FEM) applied to a series of linear springs. The title at the top reads: "Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs."

**Step 4: Apply Boundary Conditions**

The slide outlines the following steps and information:

*   **Boundary Conditions:**
    *   $x_1 = 0$ (left end of connected series is fixed)(node) $F_1=0$
*   **Apply global numbering scheme $\rightarrow k's = 1$**

**Matrix Equation**

A matrix equation is provided:

$\begin{bmatrix} 2 & -1 &   &   &   \\ -1 & 2 & -1 &   &   \\   & -1 & 2 & -1 &   \\   &   & -1 & 2 & -1 \\   &   &   & -1 & 1 \end{bmatrix} \begin{Bmatrix} x_2 \\ x_3 \\ x_4 \\ x_5 \end{Bmatrix} = \begin{Bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ F \end{Bmatrix}$

**Key Points:**

*   Only one external force at node 5.

The slide number "22" is displayed in the bottom-right corner.

### Slide 23

The image presents a detailed slide from a lecture on the Finite Element Method (FEM), specifically focusing on the deformation of a series of linear springs. The title, "Example 3. Solution. FEM.1D. Deformation of Series of Linear Springs," is prominently displayed at the top in blue text.

**Step 5: Generate Solutions (when F = 1)**

* The equation for generating solutions is provided in red handwriting-style text:
  * $x_2 = 1$, $x_3 = 2$, $x_4 = 3$, $x_5 = 4$

**Step 6: Postprocessing - Graphical Representation of Displacements**

* A diagram illustrates the initial setting of connected springs and the system after the application of a constant force.
* The diagram features:
	+ A blue line representing the springs, with five points labeled 2, 3, 4, and 5.
	+ Red handwritten text indicating the displacements at each point: $x_2 = 1$, $x_3 = 2$, $x_4 = 3$, and $x_5 = 4$.
	+ A black arrow labeled "F" representing the applied force.
	+ A wall on the left side, represented by a vertical line with diagonal hatching.

The slide number "23" is displayed in small gray text at the bottom right corner. Overall, the image provides a clear and detailed explanation of the FEM solution for a series of linear springs under a constant force.

### Slide 24

The image presents a lecture slide titled "You Try 3. FEM.1D. Deformation of Series of Linear Springs" in red text at the top.

Below the title, a paragraph of black text reads: "In previous example, consider the stiffness of each spring is different:".

A diagram follows, featuring a series of four springs connected in line, with each spring labeled with a different stiffness value (k1, k2, k3, and k4) and an external force F applied to the right end. The springs are represented by blue lines with coils, and the force F is depicted as a black arrow pointing to the right. The left end of the spring system is attached to a wall, indicated by a vertical line with diagonal hatching.

Two questions are posed below the diagram:

1) What is the general form of assembled (global) stiffness matrix?
2) What are the displacements if stiffness values from left to right are 2, 3, 4, 5 N/m and the applied external force is F = 10 N?

In the bottom-right corner, the number "24" is displayed in small gray text. The background of the slide is white.

### Slide 25

The image presents a detailed diagram and mathematical representation of the deformation of a series of linear springs using the Finite Element Method (FEM) in one dimension. The title, "You Try 3. Solution. FEM.1D. Deformation of Series of Linear Springs," is prominently displayed at the top.

**Diagram:**

*   A series of four springs connected end-to-end, each labeled with a spring constant (k1, k2, k3, k4).
*   The springs are represented by blue coils, and the connections between them are depicted as small circles.
*   A force F is applied to the rightmost spring, indicated by a black arrow pointing to the right.
*   The leftmost spring is attached to a fixed point, represented by a vertical line with diagonal hatching.

**Mathematical Representation:**

*   The global stiffness matrix is assembled from the element stiffness matrices of each spring.
*   Each element stiffness matrix is a 2x2 matrix, represented as:

    *   Element 1: $\begin{bmatrix} k_1 & -k_1 \\ -k_1 & k_1 \end{bmatrix}$
    *   Element 2: $\begin{bmatrix} k_2 & -k_2 \\ -k_2 & k_2 \end{bmatrix}$
    *   Element 3: $\begin{bmatrix} k_3 & -k_3 \\ -k_3 & k_3 \end{bmatrix}$
    *   Element 4: $\begin{bmatrix} k_4 & -k_4 \\ -k_4 & k_4 \end{bmatrix}$

These matrices are added together to form the global stiffness matrix, which represents the combined stiffness of the series of springs.

**Key Points:**

*   The problem involves finding the deformation of a series of linear springs using the Finite Element Method.
*   The diagram illustrates the physical setup, and the mathematical representation provides a detailed breakdown of the stiffness matrices for each element.
*   The global stiffness matrix is assembled by adding the element stiffness matrices, allowing for the calculation of the deformation of the springs under the applied force F.

### Slide 26

The image presents a detailed diagram and matrix representation of a finite element method (FEM) problem, specifically focusing on the deformation of a series of linear springs. The title at the top reads, "You Try 3. Solution. FEM.1D. Deformation of Series of Linear Springs."

**Diagram:**

*   A series of four springs with spring constants $k_1$, $k_2$, $k_3$, and $k_4$ are connected in series.
*   The springs are attached to a wall on the left side and have an external force $F$ applied to the rightmost end.
*   There are three internal nodes marked with red circles.

**Matrix Representation:**

*   A square matrix is drawn below the diagram, representing the stiffness matrix for the system.
*   The matrix has a size of 4x4, indicating that there are four nodes in the system (including the wall as a fixed node).
*   The diagonal elements of the matrix represent the internal nodes, with each element being the sum of the spring constants connected to that node.
*   The off-diagonal elements represent the coupling between nodes, with negative values indicating the spring constants connecting adjacent nodes.

**Matrix Elements:**

*   The matrix elements are labeled as follows:
    *   $k_1$ on the top-left corner
    *   $-k_1$ on the first row, second column
    *   $k_1 + k_2$ on the second row, second column
    *   $-k_2$ on the second row, third column
    *   $k_2 + k_3$ on the third row, third column
    *   $-k_3$ on the third row, fourth column
    *   $k_3 + k_4$ on the fourth row, fourth column
    *   $-k_4$ on the fourth row, fourth column

**Handwritten Notes:**

*   A handwritten note at the bottom of the image states, "note that all diagonal matrix elements that are representative of internal nodes - the k values one are summed."

Overall, the image provides a clear and detailed representation of the FEM formulation for a series of linear springs, highlighting the stiffness matrix and its elements.

### Slide 27

The image presents a slide with a title and two method names, set against a gradient background that transitions from white at the top to light blue at the bottom.

*   The title is prominently displayed in large, dark blue text near the top of the slide:
    *   "Application of Finite-Element Methods for"
    *   "Boundary-Value ODE"
    *   "of Heated Insulated Rod"
    *   "using:"
*   Below the title, two methods are listed in slightly smaller dark blue text:
    *   "Direct Method &"
    *   "Method of Weighted Residuals"

The slide appears to be an introduction to a presentation on applying finite-element methods to solve boundary-value ordinary differential equations (ODEs) related to a heated insulated rod, specifically using the direct method and the method of weighted residuals. There are no equations, formulas, definitions, bullet points, diagrams, or images on this slide.

### Slide 28

The image presents a lecture slide focused on the Finite Element Method (FEM) applied to a 1D heated insulated rod problem. The slide is titled "Example 4. FEM. 1D. Heated Insulated Rod."

**Problem Statement:**

*   The ends of a 10-cm insulated rod are held at fixed temperatures of $40^\circ C$ and $200^\circ C$.
*   The system is modeled by the one-dimensional Poisson's equation: $\frac{d^2T}{dx^2} = -f(x)$, where $f(x) = 10$ defines a uniform heat source along the rod.

**Task:**

*   Divide the rod into 4 equal-length elements (5 nodes) and find the temperatures $T$ at the inner nodes (2,3,4) and $\frac{dT}{dx}$ at the end nodes (1,5).
*   Develop the FEM element equation once with the direct method and once with the method of weighted residual (MWR).

**Boundary Conditions:**

*   $T(0,t) = T_1 = 40^\circ C$
*   $T(L,t) = T_2 = 200^\circ C$

**Diagram:**

*   A light blue oval represents the rod, with a dark blue line inside indicating the rod itself.
*   The rod has a length of 10 cm and is divided into 4 equal elements, resulting in 5 nodes.
*   Node 1 is located at the left end of the rod, and node 5 is at the right end.
*   The diagram includes labels for the boundary conditions and the uniform heat source.

**Key Points:**

*   The problem involves solving a 1D heat transfer problem using the Finite Element Method.
*   The system is governed by Poisson's equation with a uniform heat source.
*   The task is to find the temperatures at the inner nodes and the temperature gradients at the end nodes.

### Slide 29

The image presents a detailed solution to a problem involving the finite element method (FEM) for a heated insulated rod. The title, "Example 4. Solution. FEM. 1D. Heated Insulated Rod," is prominently displayed at the top.

**Equations and Formulas**

* The exact solution of T is given by the differential equation: $\frac{d^2T}{dn^2} = -10$ with $f(n)=10$
* The assumed solution is: $T = an^2 + bn + c \rightarrow T'' = 2a$
* The following equations are derived:
	+ $a = -5$
	+ $40 = -5(0)^2 + b(0) + c \rightarrow c = 40$
	+ $200 = -5(10)^2 + b(10) + 40$
* The values of $a$, $b$, and $c$ are solved:
	+ $a = -5$
	+ $b = 66$
	+ $c = 40$
* The final solution for T is: $T = -5x^2 + 66x + 40$

**Graph**

* A graph of the exact solution of T is provided, showing the relationship between T and x.
* The graph features:
	+ A black curve representing the solution
	+ A light blue background
	+ A red border
	+ Axes labeled:
		- x-axis: $x$ (with values ranging from 0 to 10)
		- y-axis: $T$ (with values ranging from 0 to 200)

**Additional Text**

* The text "Graph of exact solution of T →" is written in blue at the bottom of the image, accompanied by a blue arrow pointing to the graph.

### Slide 30

The image presents a slide from a presentation on the Finite Element Method (FEM) for solving a 1D heated insulated rod problem. The title of the slide is "Example 4. Solution. FEM. 1D. Heated Insulated Rod."

**Step 1: Discretization**

The first step in the FEM process is discretization, which involves dividing the rod into smaller elements and nodes. In this case, the rod is divided into:

* 4 equal-length elements
* 5 nodes

The nodes are numbered from 1 to 5, and the elements are numbered from 1 to 4.

**Diagram**

The diagram shows a light blue rectangle with a red border, representing the rod. The x-axis is labeled, and the left and right ends of the rod are labeled as $x=0$ and $x=L$, respectively. The temperature at these ends is represented by $T(0,t)$ and $T(L,t)$.

The diagram also shows:

* A function $f(x)$ representing the heat source
* Four wavy arrows indicating heat transfer
* Five nodes labeled from 1 to 5
* Four elements labeled from 1 to 4

**Note**

A note at the bottom of the slide mentions that later on, before assembling, the global numbering will be used.

**Overall**

The slide provides a clear and concise overview of the discretization step in the FEM process for a 1D heated insulated rod problem. It sets the stage for further analysis and calculation of the temperature distribution along the rod.

### Slide 31

The image presents a detailed lecture slide focused on shape functions and element equations, likely from a course on finite element methods in engineering or a related field. The slide is divided into two main sections: mathematical equations and diagrams.

**Mathematical Equations:**

The left side of the slide lists several key equations related to shape functions and element equations:

1. **Shape Functions:**
   - $N_1 = \frac{x_2 - x}{x_2 - x_1}$
   - $N_2 = \frac{x - x_1}{x_2 - x_1}$

2. **Derivatives of Shape Functions:**
   - $\frac{dN_1}{dx} = -\frac{1}{x_2 - x_1}$
   - $\frac{dN_2}{dx} = \frac{1}{x_2 - x_1}$

3. **Element Equation:**
   - $u = N_1u_1 + N_2u_2$

4. **Derivative of $u$:**
   - $\frac{du}{dx} = \frac{dN_1}{dx}u_1 + \frac{dN_2}{dx}u_2$
   - $\frac{du}{dx} = \frac{1}{x_2 - x_1}(-u_1 + u_2)$

5. **Boundary Conditions for $N_1$:**
   - $N_1(x_2) = 0$ and $N_1(x_1) = 1$

6. **Integrals:**
   - $\int_{x_1}^{x_2} Nu dx = \frac{1}{2}(x_2 - x_1)u$
   - $\int_{x_1}^{x_2} u dx = \frac{u_1 + u_2}{2}(x_2 - x_1)$

**Diagrams:**

The right side of the slide features a light blue box containing four diagrams labeled (a) through (d), which illustrate the concepts:

- **Diagram (a):** A simple line element with two nodes labeled Node 1 and Node 2.
- **Diagram (b):** A graph showing a linear variation of $u$ between $u_1$ and $u_2$.
- **Diagram (c):** A plot of $N_1$, which linearly decreases from 1 at $x_1$ to 0 at $x_2$.
- **Diagram (d):** A plot of $N_2$, which linearly increases from 0 at $x_1$ to 1 at $x_2$.

These diagrams visually represent how shape functions $N_1$ and $N_2$ interpolate between the nodal values $u_1$ and $u_2$ to define the element equation for $u$ within the element. The slide provides a comprehensive overview of the mathematical formulation and graphical representation of linear shape functions in the context of finite element analysis.

### Slide 32

The image presents a detailed slide from a lecture on the Finite Element Method (FEM) applied to a 1D heated insulated rod problem. The slide is divided into sections, each addressing a specific step or concept in solving the problem.

**Title and Step Description**

*   **Title**: "Example 4. Solution. FEM. 1D. Heated Insulated Rod."
*   **Step Description**: "Step 2. Element Equation"

**Equation and Approximation**

*   The equation provided is: $\widetilde{T} = N_1 T_1 + N_2 T_2$
*   This equation represents an approximation using linear interpolation functions.

**Diagram Description**

*   A diagram is shown with a light blue background and a red outline, representing an element of the rod.
*   The diagram has two nodes labeled "Node 1" and "Node 2".
*   The nodes are connected by a line with an arrow pointing downwards, indicating the direction of heat flow.
*   The diagram also shows the temperature $T$ at Node 1 and Node 2, with $T_1$ and $T_2$ respectively.
*   The x-axis is labeled with $x_1$ and $x_2$, representing the coordinates of Node 1 and Node 2.

**Direct Approach Description**

*   The direct approach is described as: "we do it for $q=0$, $q=heat \: flux \: [cal/cm^2.s]$"

**Fourier's Law**

*   Fourier's Law is stated as: $q=-k' \frac{dT}{dx}$
*   This law relates the heat flux $q$ to the temperature gradient $\frac{dT}{dx}$ and the coefficient of thermal conductivity $k'$.

**Heat Flux Equations**

*   Two heat flux equations are derived:
    *   $q_1=k' \frac{T_1-T_2}{x_2-x_1}$ at node 1
    *   $q_2=k' \frac{T_2-T_1}{x_2-x_1}$ at node 2
*   These equations express the heat flux at each node in terms of the temperatures at the nodes and the coefficient of thermal conductivity $k'$.

**Additional Notes**

*   The coefficient of thermal conductivity $k'$ is defined as: $[cal/s.cm.^{\circ}C]$
*   The heat flux at each node is also expressed as: $q_1=-k' \frac{dT(x_1)}{dx}$, $q_2=-k' \frac{dT(x_2)}{dx}$

### Slide 33

The image presents a slide from a presentation on the Finite Element Method (FEM), specifically focusing on a 1D heated insulated rod. The title, "Example 4. Solution. FEM. 1D. Heated Insulated Rod," is prominently displayed at the top in blue text.

**Equation and Matrix**

The central element of the slide is an equation that reads:

$\frac{1}{x_2-x_1} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \begin{Bmatrix} T_1 \\ T_2 \end{Bmatrix} = \begin{Bmatrix} -\frac{dT(x_1)}{dn} \\ \frac{dT(x_2)}{dn} \end{Bmatrix}$

This equation is accompanied by two labels:

*   **Element Stiffness Matrix**: $\frac{1}{x_2-x_1} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$
*   **Boundary Condition**: $\begin{Bmatrix} -\frac{dT(x_1)}{dn} \\ \frac{dT(x_2)}{dn} \end{Bmatrix}$

**Additional Text**

Below the equation, the text "Element Equation: Direct Approach" appears in blue. Further down, the statement "Matrix can describe the behaviour of a typical element in our system" is written in black.

**Slide Details**

In the bottom-right corner, the number "33" is visible, indicating that this is likely the 33rd slide in the presentation. The background of the slide is white, providing a clean and clear visual environment for the equation and text. Overall, the slide effectively communicates a key concept in the Finite Element Method, specifically in the context of a 1D heated insulated rod.

### Slide 34

The image presents a detailed lecture slide focused on the Finite Element Method (FEM) applied to a 1D heated insulated rod problem. The slide is divided into several sections, each addressing a specific aspect of the solution.

**Title and Initial Equation**

*   The title of the example is "Example 4. Solution. FEM. 1D. Heated Insulated Rod."
*   The initial equation provided is $\frac{d^2 T}{dx^2} + f(x) \rightarrow f(x) = 0$, which simplifies to $R = \frac{d^2 \tilde{T}}{dx^2} + f(x)$, where $R$ represents the residual.

**Method of Weighted Residual (MWR)**

*   The Method of Weighted Residual (MWR) is introduced as a technique for solving the problem.
*   The equation for MWR is:

    $\frac{1}{x_2 - x_1} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \{T\} = \begin{cases} -\frac{dT(x_1)}{dx} \\ \frac{dT(x_2)}{dx} \end{cases} + \begin{cases} \int_{x_1}^{x_2} f(x)N_1(x) dx \\ \int_{x_1}^{x_2} f(x)N_2(x) dx \end{cases}$

    This equation is broken down into three components:
    *   **Element Stiffness Matrix**: $\frac{1}{x_2 - x_1} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$
    *   **Boundary Condition**: $\begin{cases} -\frac{dT(x_1)}{dx} \\ \frac{dT(x_2)}{dx} \end{cases}$
    *   **External effects**: $\begin{cases} \int_{x_1}^{x_2} f(x)N_1(x) dx \\ \int_{x_1}^{x_2} f(x)N_2(x) dx \end{cases}$

**Additional Information**

*   It is noted that $N_1$ and $N_2$ are linear interpolation functions.

**Slide Details**

*   The slide number is 34, indicating it is part of a larger presentation.

### Slide 35

The image presents a lecture slide focused on the Finite Element Method (FEM) for solving a 1D heated insulated rod problem. The slide is divided into sections, each addressing a specific step in the solution process.

**Title and Problem Statement**

*   The title of the slide is "Example 4. Solution. FEM. 1D. Heated Insulated Rod."
*   The problem involves using the method of weighted residuals (MWR) to solve for the temperature distribution in a 1D heated insulated rod.
*   Given:
    *   $f(x) = 10$
    *   $T(0) = 40$
    *   $T(10) = 200$

**Step 1: Discretization**

*   The rod is divided into 4 equal-sized elements, each with a length of $2.5$ cm.

**Step 2: Evaluate External Effects (Heat Source Terms) for Element #1**

*   The slide provides two integral equations for evaluating external effects (heat source terms) for element #1:
    *   $\int_{x_1}^{x_2} f(x)N_1(x) dx = \int_{0}^{2.5} (10) \left(\frac{2.5-x}{2.5}\right) dx = 12.5$
    *   $\int_{x_1}^{x_2} f(x)N_2(x) dx = \int_{0}^{2.5} (10) \left(\frac{x-0}{2.5}\right) dx = 12.5$

**Diagrams and Images**

*   There are no diagrams or images on the slide, only text and equations.

**Summary**

The slide outlines the steps to solve a 1D heated insulated rod problem using the Finite Element Method (FEM) with the method of weighted residuals (MWR). It provides the problem statement, discretization of the rod into elements, and the evaluation of external effects (heat source terms) for element #1. The slide presents two integral equations for element #1, which are solved to obtain the values of $12.5$ for both integrals.

### Slide 36

The image presents a detailed lecture slide focused on the Finite Element Method (FEM) applied to a 1D heated insulated rod problem. The slide is divided into two main sections, each addressing a specific step in the solution process.

### **Section 1: Development of Element Stiffness Matrix**

*   **Title:** Example 4. Solution. FEM. 1D. Heated Insulated Rod.
*   **Step 3: Develop element stiffness matrix of element #1 (x1=0, x2=2.5)**
    *   The formula for the element stiffness matrix is provided as:

        $\frac{1}{x_2-x_1}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} = 0.4\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$

### **Section 2: Equations and Unknowns per Element**

*   **Step 4: Give 2 equations, unknowns per element**
    *   A general equation is presented:

        $\frac{1}{x_2-x_1}\begin{bmatrix} -1 & 1 \\ -1 & 1 \end{bmatrix}\{T\} = \begin{Bmatrix} -\frac{dT(x_1)}{dn} \\ \frac{dT(x_2)}{dx} \end{Bmatrix} + \begin{Bmatrix} \int_{x_1}^{x_2} f(x)N_1(x) dx \\ \int_{x_1}^{x_2} f(x)N_2(x) dx \end{Bmatrix}$

    *   This is then applied to the specific case, resulting in two equations:

        $\begin{Bmatrix} 0.4 T_1-0.4 T_2= -\frac{dT(x_1)}{dn} + 12.5 \\ -0.4 T_1 +0.4 T_2= \frac{dT(x_2)}{dn} + 12.5 \end{Bmatrix}$

**Summary:**

*   The slide outlines the process of developing an element stiffness matrix for a 1D heated insulated rod using the Finite Element Method.
*   It provides a specific example with $x_1=0$ and $x_2=2.5$, leading to a stiffness matrix of $0.4\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$.
*   The application of this matrix to form equations for unknowns per element is demonstrated, resulting in a system of two equations involving $T_1$ and $T_2$.

### Slide 37

The image presents a slide from a presentation on the Finite Element Method (FEM) for a 1D heated insulated rod problem. The title of the slide is "Example 4. Solution. FEM. 1D. Heated Insulated Rod." The main points are:

* **Assemble element equations: Define global numbering system**
	+ A diagram showing a rod with five nodes and four elements is provided.
	+ The local and global numbering systems are illustrated.
	+ The local numbering system ranges from 1 to 2 for each element, while the global numbering system ranges from 1 to 5.
* **System Topology**
	+ A table is presented to describe the system topology.
	+ The table has four columns: Element #, Local, and Global.
	+ The table shows the local and global node numbers for each element.

The table contains the following data:

| Element # | Local | Global |
| --- | --- | --- |
| 1 | 1 2 | 1 2 |
| 2 | 1 2 | 2 3 |
| 3 | 1 2 | 3 4 |
| 4 | 1 2 | 4 5 |

The slide provides a clear and concise overview of the system topology and the assembly of element equations for the 1D heated insulated rod problem using the Finite Element Method.

### Slide 38

The image presents a detailed example of a solution using the Finite Element Method (FEM) for a 1D heated insulated rod. The title, "Example 4. Solution. FEM. 1D. Heated Insulated Rod," is prominently displayed at the top.

**Equations and Matrix Assembly**

The slide begins by presenting two equations:

*   $0.4T_{1}-0.4T_{2} = -\frac{dT(x_{1})}{dx} + 12.5$
*   $-0.4T_{1}+0.4T_{2} = \frac{dT(x_{2})}{dx} + 12.5$

These equations are accompanied by a red oval highlighting the derivatives.

**Element #1 Matrix**

The first matrix, labeled "Element #1," is a 3x3 matrix with the following structure:

| 0.4  | -0.4 | 0    | 
| ---- | -----| ---- |
| -0.4 | 0.4  | 0    | 
| 0    | 0    | 0    |

This matrix is multiplied by a vector of temperatures $\{T_1, T_2, 0, 0, 0\}^T$ and set equal to a vector of external effects:

$\begin{bmatrix} 0.4  & -0.4 & 0    & 0 & 0 \\ -0.4 & 0.4  & 0    & 0 & 0 \\ 0    & 0    & 0    & 0 & 0 \\ 0    & 0    & 0    & 0 & 0 \\ 0    & 0    & 0    & 0 & 0 \end{bmatrix} \begin{Bmatrix} T_1 \\ T_2 \\ 0 \\ 0 \\ 0 \end{Bmatrix} = \begin{Bmatrix} -\frac{dT(x_1)}{dx} + 12.5 \\ \frac{dT(x_2)}{dx} + 12.5 \\ 0 \\ 0 \\ 0 \end{Bmatrix}$

**Element #2 Matrix**

The second matrix, labeled "Add Element #2," is also a 3x3 matrix:

| 0.4  | -0.4 | 0    | 
| ---- | -----| ---- |
| -0.4 | 0.4+0.4 | -0.4 | 
| 0    | -0.4 | 0.4  |

This matrix is multiplied by a vector of temperatures $\{T_1, T_2, T_3, 0, 0\}^T$ and set equal to a vector of external effects:

$\begin{bmatrix} 0.4  & -0.4 & 0    & 0 & 0 \\ -0.4 & 0.4+0.4 & -0.4 & 0 & 0 \\ 0    & -0.4 & 0.4  & 0 & 0 \\ 0    & 0    & 0    & 0 & 0 \\ 0    & 0    & 0    & 0 & 0 \end{bmatrix} \begin{Bmatrix} T_1 \\ T_2 \\ T_3 \\ 0 \\ 0 \end{Bmatrix} = \begin{Bmatrix} -\frac{dT(x_1)}{dx} + 12.5 \\ 12.5+12.5 \\ \frac{dT(x_3)}{dx} + 12.5 \\ 0 \\ 0 \end{Bmatrix}$

**Note**

A note at the bottom of the slide reads: "Internal boundary conditions cancel each other (see 2nd row of external effect matrix)."

### Slide 39

The image presents a detailed mathematical representation of a solution to an example problem, specifically Example 4, related to the Finite Element Method (FEM) applied to a 1D heated insulated rod. The content is structured into two main sections: the first part illustrates the process of assembling matrices for elements 3 and 4, while the second part shows the final assembled matrix.

### Detailed Description:

#### Title and Introduction
- **Title:** "Example 4. Solution. FEM. 1D. Heated Insulated Rod." in blue text at the top.
- **Instruction:** Below the title, in black text, it reads, "Continue this for elements 3 and 4 to assemble all matrices:"

#### First Section: Assembling Matrices for Elements
- This section contains a large matrix equation. The matrix on the left side is a 5x5 matrix, with most entries being zero except for a 3x3 submatrix in the middle that has handwritten red values. This matrix represents the stiffness or coefficient matrix for the assembled system up to elements 1 and 2.
- The matrix is multiplied by a column vector of temperatures \(T_1, T_2, T_3, T_4, T_5\) to yield a column vector on the right side of the equation.
- The right-hand side vector has entries that include terms like \(-dT(x_1)/dn + 12.5\), \(12.5 + 12.5\), \(12.5 + 12.5\), \(17.5 + 12.5\), and \(dT(x_5)/dn + 12.5\), indicating boundary conditions and heat fluxes at different points.

#### Second Section: Final Assembled Matrix
- **Heading:** "Finally:" in blue text.
- This section displays the fully assembled 5x5 matrix with red handwritten entries. The matrix has a symmetric structure with diagonal and off-diagonal entries.
- The assembled matrix is then multiplied by the same column vector of temperatures \(T_1, T_2, T_3, T_4, T_5\).
- The right-hand side of the equation shows a column vector with entries:
  - \(-dT(x_1)/dn + 12.5\)
  - \(25\)
  - \(25\)
  - \(25\)
  - \(dT(x_5)/dn + 12.5\)

### Equations and Formulas
The image includes matrix equations of the form:
\[ \mathbf{K} \mathbf{T} = \mathbf{F} \]
where:
- \(\mathbf{K}\) is the stiffness matrix (or coefficient matrix),
- \(\mathbf{T}\) is the vector of nodal temperatures,
- \(\mathbf{F}\) is the load vector (or force vector in structural problems, but here related to heat fluxes and boundary conditions).

### Definitions
- **FEM (Finite Element Method):** A numerical method for solving partial differential equations (PDEs) in various fields, including heat transfer.
- **1D Heated Insulated Rod:** A simplified model used to demonstrate heat transfer in one dimension.

### Diagrams/Images
- The image contains handwritten matrices and vectors, likely drawn or written during a lecture or for illustrative purposes. There are no graphical diagrams beyond these mathematical representations. 

### Conclusion
The image provides a step-by-step solution to an example problem in the context of applying the Finite Element Method to a 1D heated insulated rod. It demonstrates how to assemble element matrices into a global matrix and vector for solving the temperature distribution along the rod, taking into account boundary conditions.

### Slide 40

The image presents a mathematical problem related to the Finite Element Method (FEM) for a 1D heated insulated rod. The problem is titled "Example 4. Solution. FEM. 1D. Heated Insulated Rod." The main content of the image is a system of linear equations, which are:

* $\frac{dT(x_1)}{dx} - 0.4T_2 = -3.5$
* $0.8 T_2 - 0.4 T_3 = 25 + 0.4(40) = 41$
* $-0.4 T_2 + 0.8 T_3 - 0.4 T_4 = 25$
* $-0.4 T_3 + 0.8 T_4 = 25 + 0.4(200) = 105$
* $-0.4 T_4 - \frac{dT(x_5)}{dx} = 12.5 - 0.4(200) = -67.5$

These equations are written in black text, with some handwritten-style annotations in red ink. The background of the image is white.

There are no diagrams or images on the slide, only text and equations. The slide number "40" is displayed in the bottom-right corner. 

Overall, the image appears to be a lecture slide or a page from a textbook, presenting a specific example of applying the Finite Element Method to solve a problem involving a heated insulated rod.

### Slide 41

The image presents a detailed solution to Example 4, focusing on the Finite Element Method (FEM) applied to a 1D heated insulated rod. The content is organized into two main sections: a set of equations and a graph.

**Equations Section:**

*   The title "Example 4. Solution. FEM. 1D. Heated Insulated Rod." is displayed in blue text at the top.
*   Below the title, a handwritten note in red text reads, "Can find heat flow at the boundaries from results:"
*   A list of equations is provided, written in black and red text:
    *   $\frac{dT}{dx}(x_1) = 66$
    *   $T_2 = 173.75$
    *   $T_3 = 245$
    *   $T_4 = 253.75$
    *   $\frac{dT}{dx}(x_5) = -34$

**Graph Section:**

*   A line graph is presented, featuring two curves:
    *   A blue curve labeled "Finite-element"
    *   A black curve labeled "Analytical"
*   The graph has the following characteristics:
    *   The x-axis is labeled with values ranging from 0 to 10, with increments of 1.
    *   The y-axis is labeled with values ranging from 0 to 200, with increments of 100.
    *   The graph shows the temperature distribution along the rod, with the finite-element method and analytical solutions plotted for comparison.

**Additional Information:**

*   The background of the image is white.
*   In the bottom-right corner, the number "41" is displayed.

Overall, the image provides a clear and detailed representation of the solution to Example 4, showcasing the application of the Finite Element Method to a 1D heated insulated rod problem.

### Slide 42

The image presents a slide from a presentation, likely used in an educational setting, particularly in a course focused on numerical methods for engineers. The slide is titled "References" and provides information about the textbook used, along with an outline of specific sections related to partial differential equations and the finite-element method.

*   **Title and Textbook Information**
    *   The title "References" is prominently displayed at the top of the slide.
    *   Below the title, the textbook is cited as "Numerical Methods for Engineers" by S. Chapra and R. Canale, 7th Edition, 2015.
*   **Outline of Sections**
    *   The slide outlines sections from Part 8, which focuses on Partial Differential Equations.
    *   The sections listed include:
        *   Chapter 31: Finite-Element Method
            *   Section 31.2: Finite Element Application in One-Dimension
        *   Chapter 32: Case Studies: Partial Differential Equations
            *   Section 32.4: Finite Element Solution of a Series of Linear Springs
*   **Slide Number**
    *   The slide number, 42, is located at the bottom right corner of the slide.

In summary, this slide serves as a reference for a lecture on partial differential equations, specifically highlighting the use of the finite-element method. It references a widely used textbook in the field and outlines key sections that will be covered, providing a clear structure for the lecture material.

### Slide 43

The image presents a simple, text-based slide with the following content:

* The text "The End of Lecture" is prominently displayed in a large, black serif font.
	+ The text is centered on the slide.
	+ The font size of "The End" is larger than "of Lecture", which is positioned directly below it.
* The background of the slide is plain white.

There are no equations, formulas, definitions, bullet points, diagrams, or images present on the slide. The slide appears to be a conclusion slide, indicating the end of a lecture.

