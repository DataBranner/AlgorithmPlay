## Lattice paths: Traversing a grid without backtracking.

The model for this problem comes from Laakman fifth ed. problem 9.2, first half:

> Imagine a robot sitting on the upper-left corner of an X x Y grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot to go from (0,0) to (X,Y)?

Run in interpreter as

    import robot_on_grid as R
    R.main(X,Y)

The program first calculates the answer as a combinatorics problem: number of paths = `C(X+Y, X)` and then enumerates all the solutions and counts them. For `X+Y < 11`, the time required for the enumeration component on my computer is unreasonably long.

In truth, neither of these solutions is being done as expected in the Laakman book — the solution is supposed to involve dynamic programming.

Finally, the program confirms that the combinatoric and enumerated solutions are the same.

[end]
