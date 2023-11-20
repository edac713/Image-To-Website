# webDEV

This is just a placeholder :p

## ACTION SCHEMA

```yaml

openapi: "3.0.0"
info:
  version: "1.0.0"
  title: GitHub Pages Deployment Action
servers:
  - url: https://api.github.com
paths:
  /repos/edac713/webDEV/contents/index.html:
    get:
      summary: Get contents of the index.html to retrieve its SHA
      operationId: getFileContents
      tags:
        - repository
      responses:
        '200':
          description: index.html details retrieved
          content:
            application/json:
              schema:
                type: object
                properties:
                  sha:
                    type: string
                    description: The SHA hash of the index.html
        '404':
          description: index.html not found
    put:
      summary: Create or update the index.html in the repository using SHA
      operationId: createOrUpdateIndexHtml
      tags:
        - repository
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: The commit message
                content:
                  type: string
                  description: The content of the index.html, in Base64 encoding
                sha:
                  type: string
                  description: The SHA of the index.html to update
                branch:
                  type: string
                  description: The branch to commit to
              required:
                - message
                - content
                - sha
      responses:
        '200':
          description: index.html successfully created or updated
        '401':
          description: Unauthorized
        '422':
          description: Validation failed
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
  schemas: {}
security:
  - bearerAuth: []

```
