
function Inverse_check(A)
[m,n] = size(A);
if m~=n
    disp("A is not a square matrix, therefore inverse do not exist")
    return
end
b = zeros(size(A,1)); % identity matrix
for i= 1:size(b,1)
    b(i,i) = 1;
end
b
Aug =[A  b];
[m, n] = size (Aug);
z = size(b,2)
Aug = RowreducedEF(Aug);
    if Aug(m,m)==0
        disp('A is singular. Inverse do not exist')
        return
    else
        Inverse = Aug(:,n-z+1:n);
disp('Inverse of the matrix: ')
Inverse
    end
end