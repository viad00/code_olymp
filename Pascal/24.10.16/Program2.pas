var
  a, b, c, n, i,j: int64;
  gg: boolean;

begin
  gg := false;
  j:=0;
  read(n);
  a := 1;
  b := 1;
  for i := 1 to ((n*n)-1) do
  begin
    c := a + b;
    a := b;
    b := c;
    j:=j+1;
    if c mod n = 0 then
    begin
      gg := true;
      
      break;
    end;
  end;
  if gg then write('true ',j) else write('false ',j);
end.