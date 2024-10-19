# Use the official Node.js image as a base
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies first
COPY package*.json ./

# Install dependencies
RUN npm install --silent

# Copy the rest of the application code
COPY . .

# Expose the port that the app runs on (default for Create React App is 3000)
EXPOSE 3000

# Start the application in development mode
CMD ["npm", "start"]
