function [A, jb] = RowreducedEF(A, tol)

[m,n] = size(A);

% check if A elements are ratios of small integers
[num, den] = rat(A);
rats = isequal(A, num./den);

% check tolerance if none was provided
if (nargin < 2)
    tol = max(m,n)*eps(class(A))*norm(A,inf); %check the magnitude of largest entry
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
      % Divide the pivot row by the pivot element
      A(i,j:n) = A(i,j:n)./A(i,j);
      % Subtract multiples of the pivot row from all the other rows
      for k = [1:i-1 i+1:m]
         A(k,j:n) = A(k,j:n) - A(k,j).*A(i,j:n);
      end
      i = i + 1;
      j = j + 1;
   end
end

% Return "rational" numbers if appropriate.
if rats
    [num, den] = rat(A);
    A = num./den;
disp('Reduced Row echelon form: ')
A
end
