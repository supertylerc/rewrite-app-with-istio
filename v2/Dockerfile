FROM golang:1.18.0-alpine3.15 as builder
WORKDIR /build
COPY go.mod /build
COPY go.sum /build
COPY main.go /build
RUN go build -o /app

FROM alpine:3.15
ENV GOTRACEBACK=single
CMD ["./app"]
COPY --from=builder /app .
