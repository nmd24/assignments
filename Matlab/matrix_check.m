function matrix_check(A)

A1=RowreducedEF(A)


if A1 == A
    disp("Matrix is already in reduced row echelon form")
else
    A2=ForwardE(A)
    if A2 == A
    disp("Matrix is already in row echelon form")
    else
    disp("Matrix is not in either reduced row echelon form or row echelon form")
    end

end
