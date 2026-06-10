import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async def capture_screenshots():
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            # Load the local index.html
            path = os.path.abspath("index.html")
            await page.goto(f"file://{path}")

            # Wait for animations
            await page.wait_for_timeout(1000)

            # Take screenshot of the hero
            await page.screenshot(path="screenshot_hero.png")

            # Scroll to tours
            await page.evaluate("document.getElementById('tours').scrollIntoView()")
            await page.wait_for_timeout(1000)
            await page.screenshot(path="screenshot_tours.png")

            # Click the first tour card to open modal
            cards = await page.query_selector_all(".tour-card")
            if cards:
                await cards[0].click()
                await page.wait_for_timeout(1000) # Wait for modal animation
                await page.screenshot(path="screenshot_modal.png")

            await browser.close()

    await capture_screenshots()

if __name__ == "__main__":
    asyncio.run(run())
