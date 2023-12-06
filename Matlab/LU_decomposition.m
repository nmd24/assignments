
function LU_decomposition (enter_number_of_N)

A = randi([1 10],enter_number_of_N)

N = length(A);
L = zeros(N,N);
U = zeros(N,N);
for a=1:N
    L(a,a) = 1;
end
U(1,:) = A(1,:);
L(:,1) = A(:,1)/U(1,1);
for i = 2:N
    for j=i:N
        U(i,j) = A(i,j) - L(i,1:i-1)*U(1:i-1,j);
    end
    for k=i+1:N
        L(k,i)= (A(k,i) - L(k,1:i-1)*U(1:i-1,i))/U(i,i);
    end
end
L
U
end