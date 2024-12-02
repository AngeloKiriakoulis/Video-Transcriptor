# Frontend Dockerfile
FROM nginx:alpine

# Copy frontend files to Nginx HTML folder
COPY . /usr/share/nginx/html

# Expose the port Nginx will run on
EXPOSE 80

# Run Nginx
CMD ["nginx", "-g", "daemon off;"]
