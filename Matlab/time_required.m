
% reduced row echelon form code

function time_required(multiplier_of_50)
% input("Enter your number: ");

row=50*multiplier_of_50
col=50*multiplier_of_50

A = randi([1 10],row,col);
b = randi([1 10],row,1);

A1 =[A  b];

[m,n] = size(A1);

z = size(b,2);
times = [];

% Elements of A1 as a ratio

[num, den] = rat(A1);
rats = isequal(A1, num./den);

% Loop over the entire matrix.
i = 1;
j = 1;
while i <= m && j <= n
    tic;
   % Find value and index of largest element in the remainder of column j
   [p, k] = max(abs(A1(i:m,j)));
   k = k+i-1;
      % Swap i-th and k-th rows
      A1([i k],j:n) = A1([k i],j:n);
      % Divide the pivot row by the pivot element
      A1(i,j:n) = A1(i,j:n)./A1(i,j);
      % Subtract multiples of the pivot row from all the other rows
      for k = [1:i-1 i+1:m]
         A1(k,j:n) = A1(k,j:n) - A1(k,j).*A1(i,j:n);
         time_elp = toc;
      end
      i = i + 1;
      j = j + 1;
times = [times, time_elp];
end

% Return "rational" numbers if appropriate
if rats
    [num, den] = rat(A1);
    A1 = num./den;
end

time_required_to_solve = sum(times)

end