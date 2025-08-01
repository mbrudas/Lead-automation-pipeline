function onFormSubmit(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Leads");
  var data = e.values;

  // Insertar nueva fila
  sheet.appendRow(data);

  // Validación de email básica
  if (!data[1].includes("@")) {
    Logger.log("Email no válido: " + data[1]);
  }
}
