var
n,i:integer;
r,x1,x2,x3,y1,y2,y3,per:real;
f:Text;

begin
Assign(f, 'input.txt');
Reset(f);
Read(f, n);
read(f, r);
Read(f, x1, y1);
x3:=x1;
y3:=y1;
per:=0;
for i:=0 to n-2 do begin
  Read(f, x2, y2);
  per:=per + Sqrt(Sqr(x2-x1)+Sqr(y2-y1));
  x1:=x2; y1:=y2;
end;
per:=per+Sqrt(Sqr(x1-x3)+Sqr(y1-y3)+Sqr(x2-x1)+Sqr(y2-y1));
per:=per+((2*Pi*r)/4)*n;
Close(f);
Rewrite(f, 'output.txt');
write(f, per:0:2);
Close(f);
end.
