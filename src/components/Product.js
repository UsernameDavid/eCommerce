import React, { useState }  from 'react';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import FavoriteIcon from '@material-ui/icons/Favorite';
import { AddShoppingCart } from '@material-ui/icons';

export default function Product() {

  const [hovered, setHovered] = useState(false);
  const toggleHover = () => setHovered(!hovered);

  const textToggleHover = () => setHovered(!hovered);

  return (
    <Card sx={{ maxWidth: 100 }}>
      <CardHeader
        action={
          <Typography 
          variant = 'h6'
          color='textSecondary'
          >
            {"€50.00"}
          </Typography>
        }
        title="Shoes"
        subheader="in Stock"
      />
      <div className="img-text-wrapper">
        <div className="img-wrapper">
          <CardMedia className={hovered ? "card-image hovered" : "card-image"}
            onMouseEnter={toggleHover}
            onMouseLeave={toggleHover}
            component="img"
            height="194"
            image="https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/910b685c-1a3d-4b5f-95fe-9a81c29ad9a6/air-force-1-07-zapatillas-whLCDz.png"
            alt="Nike Air Force 1 '07"
          />
        </div>
        <div className={hovered ? "img-description-wrapper text-hovered" : "img-description-wrapper"} onMouseEnter={textToggleHover} onMouseLeave={textToggleHover}>
          <div className="img-description">
          Your real strength lies within you, and the Nike Air Force 1 '07 is what you need to flaunt it in style. Blending hardwood comfort with off-court flair, these sneakers radiate retro perfection. The cupsole silhouette is draped in durable leather that reflects the OG boldness of the ‘80s. Iconic as ever, the Air cushioning gives you the lightest and smoothest stride ever. Featuring the classic pivot pattern for traction, the grippy translucent rubber outsole is the true companion to your excellent walk.
          </div>
        </div>
      </div>
      <CardContent>
        <Typography variant="body2" color="text.secondary">
        Nike Air Force 1 '07
        </Typography>
      </CardContent>
      <CardActions disableSpacing>
        <IconButton aria-label="add to cart">
          <AddShoppingCart />
        </IconButton>
        <IconButton aria-label="add to favorites">
          <FavoriteIcon />
        </IconButton>
      </CardActions>
    </Card>
  );
}
