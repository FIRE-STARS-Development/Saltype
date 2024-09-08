import { defineEventHandler, setHeader } from 'h3';

export default defineEventHandler((event) => {
    const method = event.node.req.method;
    const allowedOrigins = ['http://localhost:3000'];
    const origin = event.node.req.headers.origin || '';

    if (allowedOrigins.includes(origin)) {
        setHeader(event, 'Access-Control-Allow-Origin', origin);
    } else {
        setHeader(event, 'Access-Control-Allow-Origin', 'null');
    }

    setHeader(event, 'Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS');
    setHeader(event, 'Access-Control-Allow-Headers', 'Content-Type, Authorization');
    setHeader(event, 'Access-Control-Allow-Credentials', 'true');

    // プリフライトリクエストの処理
    if (method === 'OPTIONS') {
        setHeader(event, 'Access-Control-Max-Age', 86400); // 24 hours
        event.node.res.statusCode = 204;
        event.node.res.end();
        return;
    }
});