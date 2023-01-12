function matrix_row_echelon_check(A)

A1=ForwardE(A)

if A1 == A
    disp("Matrix is in row echelon form, therefore the reduced row form is: ")
    RowreducedEF(A);
else
    disp("ERROR: Matrix is not in row echelon form, " + ...
        "Please enter row echelon matrix similar to above shown for eligible reduced row form: ");
end
