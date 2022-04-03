import React, { useEffect } from 'react'

export default function useScrollToBottom(containerRef: React.RefObject<HTMLElement>) {
  useEffect(() => {
  if (containerRef && containerRef.current && containerRef.current.lastElementChild) {
      containerRef.current.lastElementChild.scrollIntoView({
        behavior: 'smooth',
      })
    }
  }, [containerRef])
}
