# Build stage
FROM node:18 AS build
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
#No build step needed

# Runtime
FROM node:18-alpine
WORKDIR /app

RUN adduser -D appuser
USER appuser

COPY --from=build /app ./

EXPOSE 3000

HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1

CMD ["npm", "start"]
