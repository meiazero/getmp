# Imagem base
FROM grafana/grafana:latest

# Diretório de trabalho
WORKDIR /usr/share/grafana

# Copiar arquivos de configuração personalizados
COPY ./custom-config.ini ./conf/custom-config.ini

# Configurar volumes
VOLUME ["/home/meiazero/Projetos/getmp/grafana/"]

# Expor a porta padrão do Grafana
EXPOSE 3000

# Comando de inicialização do Grafana
CMD ["grafana-server", "--config", "conf/custom-config.ini"]
