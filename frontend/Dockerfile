FROM nginx:alpine

# Copy HTML to nginx's default serve directory
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]