var
  i, next, j, off, n: int64;
  s: array[0..50] of integer;
  mas: array[0..9] of integer;

begin
  readln(n);
  for i := 0 to n-1 do readln(s[i]);
  println(s);
  next := 0;
  off:=0;
  if s[0] = 0 then begin next := 1; off:=1 end;
  for i := off to n do 
  begin
    for j := 1 to s[i] do 
    begin
      print(next);
    end;
    if next = 0 then begin next := 1; end
    else next := 0;
  end;
end.