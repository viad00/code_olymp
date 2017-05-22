var
  f: string;
  t: string;
  sh: int64;
  n: int64;
  hh: array [1..99] of int64;

begin
  Assign(input, 'INPUT.TXT');
  Readln(n);
  for i: int64 := 1 to n+1 do 
  begin
  hh[i]:=0;
  end;
  for i: int64 := 1 to n do 
  begin
    Readln(f);
    t := Copy(f, f.Length - 1, 2);
    sh:=StrToInt64(t);
    hh[sh]:=+1;
  end;
  Print('done');
end.