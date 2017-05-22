var
  a, m: int64;
  s: string;
  f: char;

begin
  ReadLn(s);
  Readln(f);
  m := 0;
  for a := 1 to s.Length do 
  begin
    if (s[a] = f) then m := m + 1;
  end;
  write(m);
end.