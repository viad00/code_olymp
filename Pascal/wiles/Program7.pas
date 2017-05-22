var a,b,n,diff:integer;
begin
Readln(a);
b:=a;
while a <> 0 do begin
n:=n+1;
b:=b div 10;
end;
writeln(n);
end.
                  ________
                 /  ___  |
                /  /   | |
               /  /    |
               |
              /  /     | |
             / _/      |_|