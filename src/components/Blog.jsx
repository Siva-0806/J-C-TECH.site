import React from 'react';

const blogPosts = [
  {
    id: 'ai-drawing-search',
    tag: 'AI',
    title: 'How AI Is Changing Drawing Search on the Shop Floor',
    description: "A practical look at why search, not automation, is AI's first real win in manufacturing.",
    image: '/blogs/How AI Is Changing Drawing Search on the Shop Floor.jpeg',
    pdfUrl: '/blogs/how-ai-is-changing-drawing-search.pdf',
    fileName: 'How-AI-Is-Changing-Drawing-Search.pdf',
  },
  {
    id: 'bms-explained',
    tag: 'EV',
    title: 'Battery Management Systems, Explained for Design Engineers',
    description: 'What every mechanical engineer should know before their first EV project.',
    image: '/blogs/Battery-Management-System.jpg',
    pdfUrl: '/blogs/battery-management-systems-explained.pdf',
    fileName: 'Battery-Management-Systems-Explained.pdf',
  },
  {
    id: 'gdt-mistakes',
    tag: 'CAD',
    title: 'GD&T Mistakes That Cost Manufacturers the Most',
    description: 'The tolerancing errors we see repeated across every industry we consult for.',
    image: '/blogs/blog-gdt-cad.jpg',
    pdfUrl: '/blogs/gdt-mistakes-that-cost-manufacturers.pdf',
    fileName: 'GDT-Mistakes-That-Cost-Manufacturers.pdf',
  },
];

const Blog = () => {
  const handleDownload = (pdfUrl, fileName) => {
    const link = document.createElement('a');
    link.href = pdfUrl;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <section id="blog">
      <div className="container">
        <div className="section-head reveal">
          <div className="eyebrow">From the Blog</div>
          <h2>Weekly Articles on What Actually Moves Engineering Forward</h2>
        </div>
        <div className="blog-grid stagger">
          {blogPosts.map((post) => (
            <div
              key={post.id}
              className="blog-card reveal"
              style={{
                display: 'flex',
                flexDirection: 'column',
                cursor: 'pointer',
              }}
              onClick={() => handleDownload(post.pdfUrl, post.fileName)}
            >
              <div className="blog-thumb">
                <img src={post.image} alt={post.title} className="blog-thumb-img" />
                <div className="blog-thumb-overlay" />
                <span className="blog-tag">{post.tag}</span>
              </div>
              <div
                className="blog-body"
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  flex: 1,
                  justifyContent: 'space-between',
                }}
              >
                <div>
                  <h4>{post.title}</h4>
                  <p>{post.description}</p>
                </div>
                <div>
                  <a
                    href={post.pdfUrl}
                    download={post.fileName}
                    className="btn-download-blog"
                    title={`Download ${post.title} as PDF`}
                    onClick={(e) => {
                      e.stopPropagation();
                    }}
                  >
                    <svg
                      width="16"
                      height="16"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2.2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      aria-hidden="true"
                    >
                      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                      <polyline points="7 10 12 15 17 10" />
                      <line x1="12" y1="15" x2="12" y2="3" />
                    </svg>
                    <span>Download Blog</span>
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Blog;
