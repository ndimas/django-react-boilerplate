# frontend/Dockerfile
FROM node:16-alpine

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Build the application with detailed logging
RUN npm run build || (echo "npm run build failed"; tail -n 1000 /app/build.log; exit 1)

EXPOSE 3000

CMD ["npm", "start"]