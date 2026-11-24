import { render, screen } from '@testing-library/react';
import App from './App';

test('renders a link to the YouTube channel on the home page', () => {
  render(<App />);
  const channelLink = screen.getByRole('link', { name: /visit our youtube channel/i });

  expect(channelLink).toHaveAttribute('href', 'https://www.youtube.com/@GitHub');
  expect(channelLink).toHaveAttribute('target', '_blank');
  expect(channelLink).toHaveAttribute('rel', 'noopener noreferrer');
});
