import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def conectar_banco(caminho_db="hospital.db"):
    return sqlite3.connect(caminho_db)


def carregar_dados(conexao):
    query = """
    SELECT 
        p.nome,
        p.idade,
        p.sexo,
        e.tipo_exame,
        e.regiao_corpo,
        r.data_exame,
        r.dose_mSv
    FROM registros_exames r
    JOIN pacientes p ON r.id_paciente = p.id_paciente
    JOIN exames e ON r.id_exame = e.id_exame
    """
    return pd.read_sql_query(query, conexao)


def resumo_estatistico(df):
    print("\nResumo estatístico da dose (mSv):")
    print(df["dose_mSv"].describe())


def calcular_dose_acumulada(df):
    dose_total = df.groupby("nome")["dose_mSv"].sum().reset_index()
    return dose_total.sort_values(by="dose_mSv", ascending=False)


def classificar_risco(df_dose, limite_anual=100):
    df_resultado = df_dose.copy()
    df_resultado["risco"] = df_resultado["dose_mSv"].apply(
        lambda x: "ACIMA DO LIMITE" if x > limite_anual else "DENTRO DO LIMITE"
    )
    return df_resultado


def gerar_grafico(df_dose, limite_anual=100):
    df_ordenado = df_dose.sort_values(by="dose_mSv", ascending=False)

    cores = [
        "red" if dose > limite_anual else "blue"
        for dose in df_ordenado["dose_mSv"]
    ]

    plt.figure()
    plt.bar(df_ordenado["nome"], df_ordenado["dose_mSv"], color=cores)
    plt.xticks(rotation=45)
    plt.title("Dose Acumulada Anual por Paciente (mSv)")
    plt.xlabel("Paciente")
    plt.ylabel("Dose Total (mSv)")
    plt.tight_layout()
    plt.show()


def main():
    conexao = conectar_banco()
    df = carregar_dados(conexao)

    resumo_estatistico(df)

    dose_total = calcular_dose_acumulada(df)
    dose_classificada = classificar_risco(dose_total)

    print("\nClassificação de risco anual:")
    print(dose_classificada)

    gerar_grafico(dose_classificada)

    conexao.close()


if __name__ == "__main__":
    main()
