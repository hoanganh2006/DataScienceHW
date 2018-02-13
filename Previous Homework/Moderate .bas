Attribute VB_Name = "Module1"
Sub change()

Dim WS As Worksheet
For Each WS In Worksheets
   Dim closing As Double
        closing = 0
   Dim opening As Double
        opening = WS.Cells(2, 3).Value
        WS.Cells(2, 12).Value = opening
   Dim Summary_Table_Row As Integer
   Summary_Table_Row = 2
   Dim change As Double
    For i = 2 To (WS.Cells(Rows.Count, 1).End(xlUp).Row - 1)

        If WS.Cells(i + 1, 1).Value <> WS.Cells(i, 1).Value Then
           closing = WS.Cells(i, 6).Value
           change = ((closing - opening) / opening) * 100
           opening = WS.Cells(i + 1, 3).Value
           WS.Cells(Summary_Table_Row, 13).Value = closing
           WS.Cells(Summary_Table_Row, 14).Value = change
           Summary_Table_Row = Summary_Table_Row + 1
           WS.Cells(Summary_Table_Row, 12).Value = opening
       Else
           closing = WS.Cells(i + 1, 6).Value
       End If
    Next i
    WS.Cells(1, 12).Value = "Open"
    WS.Cells(1, 13).Value = "Close"
   Next WS

End Sub

