FROM lambci/lambda:build-python3.8

LABEL maintainer="mahatthana.n@gmail.com"

WORKDIR /var/task

# Fancy prompt to remind you are in zappashell
RUN echo 'export PS1="\[\e[36m\]zappashell>\[\e[m\] "' >> /root/.bashrc

# Additional RUN commands here
# RUN yum clean all && \
#   yum -y install yarn

CMD ["bash"]
