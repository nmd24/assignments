% Gauss eliminalion

function A=ForwardE(A)

% To solve System Ab
% input A and b
% Output X
[m, n] = size (A);
if m~=n
    disp("A is not a square matrix")
end
C=zeros(1,n); 
% for partial pivoting in pth column 
for p=1:n-1
    [val, j]=max(abs(A(p:n,p)));
    % Val=value and j=localion
    % interchange the pth and jth rows 
    C=A(p,:); 
    A(p,:)=A(p+j-1,:);
    A(j+p-1,:)=C; 
    if A(p,p)==0
        disp('A is singular')
        break
    end
    % Elimination process for column P 
    for k=p+1:n
        M=-A(k,p)/A(p,p);
        % M=Multiplier
        A(k,p:n)=A(k,p:n)+M*A(p,p:n); 
    end
    fprintf('Gauss Elimination matrix at the pth=%d step \n',p)
    A
end
end