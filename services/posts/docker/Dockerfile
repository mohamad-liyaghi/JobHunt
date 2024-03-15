FROM golang:1.21.0-alpine

WORKDIR /backend

COPY go.mod go.mod

RUN go mod download

COPY . .