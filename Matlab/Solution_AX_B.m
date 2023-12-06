
function Solution_AX_B(A,b)

Aug =[A  b];
[m, n] = size (Aug);
[p, q] = size (A);
if p~=q
    disp("A is not a square matrix")
else
    disp("A is a square matrix")
end
z = size(b,2);

X = RowreducedEF(Aug);

    if X(p,p)==0
        disp('A is singular. No unique solution')
        return
    else
        disp('Solutions of equations: ') 
        X = X(:,n-z+1:n)
    end
end