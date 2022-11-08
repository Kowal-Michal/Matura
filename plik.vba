Sub nkat()

Dim n As Integer
Dim x As Double
Dim y As Double
Dim r As Double
Dim phi As Double
Dim alfa As Double
Dim i As Integer
Const pi As Double = 3.14

n = [b1]
x = [b2]
y = [b3]

r = Sqr(x * x + y * y)
alfa = (2 * pi) / n

If x = 0 Then
    If y > 0 Then
        phi = 0.5 * pi
    Else
        phi = 1.5 * pi
    End If
Else
    phi = Atn(y / x)
End If

Cells(1, "C").Value = x
Cells(1, "D").Value = y

For i = 0 To n
    Cells(i + 1, "C").Value = r * Cos(phi + i * alfa)
    Cells(i + 1, "D").Value = r * Sin(phi + i * alfa)
Next i

End Sub

Sub gumuj()
Dim p As Integer
For p = 1 To 100
    Cells(p, "C").Value = ""
    Cells(p, "D").Value = ""
Next p
End Sub
