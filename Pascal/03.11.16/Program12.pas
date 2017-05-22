const
  N = 30;

var
  a: array [1..N] of integer; 
  i, j: integer; 
  s: real;

begin
  Randomize();
  for i := 1 to N do begin a[i] := Random(0, 100);write(a[i], ' '); end;
  writeln();
  j := 0;
  for i := 1 to N do begin j := j + a[i]; end;
  s := j / N;
  j := 0;
  for i := 1 to N do begin if a[i] > s then begin j := j + 1 end; end;
  writeln('среднее: ', s, ' кол-во: ', j);
end.