FROM alpine:latest
RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.3/main" >> /etc/apk/repositories
RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk update
RUN apk add tar openjdk8-jre openjdk8 vim python curl git py-numpy@testing py-pip
ENV SCALA_VERSION=2.11.8 \
    SCALA_HOME=/usr/share/scala \
    SPARK_VERSION=spark-2.1.0-bin-hadoop2.7

RUN apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \
    apk add --no-cache bash && \
    cd "/tmp" && \
    wget "https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz" && \
    tar xzf "scala-${SCALA_VERSION}.tgz" && \
    mkdir "${SCALA_HOME}" && \
    rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat && \
    mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib" "${SCALA_HOME}" && \
    ln -s "${SCALA_HOME}/bin/"* "/usr/bin/" && \
    apk del .build-dependencies

ENV SBT_VERSION 0.13.11
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

# Install sbt
RUN curl -sL "http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C /usr/local && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built
RUN sbt

RUN adduser -S spark
RUN cd /home/spark
RUN wget http://d3kbcqa49mib13.cloudfront.net/${SPARK_VERSION}.tgz
RUN tar xf ${SPARK_VERSION}.tgz
RUN rm ${SPARK_VERSION}.tgz
RUN mv ${SPARK_VERSION} spark
ENV PATH ${PATH}:/spark/bin
ENV PATH ${PATH}:/spark/sbin
USER spark
WORKDIR /home/spark
