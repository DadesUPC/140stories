function typewrite(elem, time, i, text)
{
	var len = text.length;
	setTimeout(function()
	{
		elem.text = text.substring(0, i + 1);
		if (i < len - 1)
		{
			typewrite(elem, time, i + 1, text);
		}
	}, time / (len - 1));
}

typewrite(document.getElementById("subtitle"), 3, 0, "Collaborative stories 140 characters at a time.");