function loadSwagger(url) {
    const ui = SwaggerUIBundle({
      url: url,
      dom_id: '#swagger-ui',
      presets: [SwaggerUIBundle.presets.apis],
      layout: "BaseLayout"
    });
  }
  
  window.loadSwagger = loadSwagger;
  