Attribute VB_Name = "Module1"
Sub stock_volume()

Dim WS As Worksheet
For Each WS In Worksheets

   Dim ticker As String
   Dim volume As Double
       volume = 0

   Dim Summary_Table_Row As Integer
   Summary_Table_Row = 2

       For i = 2 To WS.Cells(Rows.Count, 1).End(xlUp).Row

           If WS.Cells(i + 1, 1).Value <> WS.Cells(i, 1).Value Then
           ticker = WS.Cells(i, 1).Value
           volume = volume + WS.Cells(i, 7).Value

           WS.Cells(Summary_Table_Row, 10).Value = ticker
           WS.Cells(Summary_Table_Row, 11).Value = volume
           Summary_Table_Row = Summary_Table_Row + 1
           volume = 0
       
       Else
           volume = volume + WS.Cells(i, 7).Value
   
       End If

   Next i
    WS.Cells(1, 11).Value = "Total Volume"
    WS.Cells(1, 10).Value = "Ticker"
   Next WS

End Sub
