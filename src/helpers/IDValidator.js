export function IDNumberValidator(ID_number) {
    if (!ID_number) return "Password can't be empty."
    if (ID_number.length != 13) return 'Id number must have 13 numbers.'
    return ''
  }