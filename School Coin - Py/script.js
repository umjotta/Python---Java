function redirecionar(tipo) {
  if (tipo === "aluno") {
    window.location.href = "telaAluno.html"; // Próxima tela do aluno
  } else if (tipo === "professor") {
    window.location.href = "telaProfessor.html"; // Próxima tela do professor
  }
}
