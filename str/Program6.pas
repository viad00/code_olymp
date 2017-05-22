var
  a, m: int64;
  s: string;

begin
  ReadLn(s);
  m := 0;
  for a := 2 to s.Length do 
  begin
    if (string(s[a - 1] + s[a]) = 'ах') then 
    begin
      s[a - 1] := 'у';
      s[a] := 'х';
    end;
  end;
  write(s);
end.