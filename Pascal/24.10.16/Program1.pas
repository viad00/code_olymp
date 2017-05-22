var
  m, n, i, j: integer;

begin
  Read(m, n);
  for j := m to n do
  begin
    writeln();
    write(j, ':= ');
    for i := 2 to m - 1 do
    begin
      if j mod i = 0 then
        write(i, ' ');
    end;
  end;
  
end.