var
  a: int64;
  s: string;

begin
  ReadLn(s);
  if (s[1] = s[s.Length]) then write('да') else write('нет');
end.