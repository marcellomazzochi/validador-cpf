def limpar_cpf(texto_cpf: str) -> str:
  cpf_limpo = texto_cpf.replace(".", "").replace("-","").replace(" ", "")
  return cpf_limpo
