function [A, jb] = Rowreduced_with_Elementary(A, tol)

[m,n] = size(A);

% check if A elements are ratios of small integers
[num, den] = rat(A);
rats = isequal(A, num./den);

I = zeros(n); % identity matrix
for i= 1:size(I,1)
    I(i,i) = 1;
end

% check tolerance if none was provided
if (nargin < 2)
    tol = max(m,n)*eps(class(A))*norm(A,inf);
end

% Loop over the entire matrix.
i = 1;
j = 1;
jb = zeros(1,0);
while i <= m && j <= n
   % Find value and index of largest element in the remainder of column j
   [p, k] = max(abs(A(i:m,j)));
   k = k+i-1;
   if p <= tol
      % The column is negligible, zero it out
      A(i:m,j) = 0;
      j = j + 1;
   else
      % Remember column index
      jb = [jb j]; 
      % Swap i-th and k-th rows
      A([i k],j:n) = A([k i],j:n);
      I([i k],j:n) = I([k i],j:n);
      % Divide the pivot row by the pivot element
      I(i,j:n) = I(i,j:n)./A(i,j);
      A(i,j:n) = A(i,j:n)./A(i,j);
      I(isnan(I)) = 0;
      I(isinf(I)) = 0;
      % Subtract multiples of the pivot row from all the other rows
      for k = [1:i-1 i+1:m]
         I(k,j:n) = I(k,j:n) - I(k,j).*A(i,j:n);
         A(k,j:n) = A(k,j:n) - A(k,j).*A(i,j:n);
         I(isnan(I)) = 0;
         I(isinf(I)) = 0;
      end
      i = i + 1;
      j = j + 1;
      A 
      E=I
   end
end

% Return "rational" numbers if appropriate.
if rats
    [num, den] = rat(A);
    A = num./den;
disp('Reduced Row echelon form: ')
A
end
